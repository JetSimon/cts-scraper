import os
import re
import urllib.request
from urllib.request import urlretrieve
from urllib.parse import urlparse
from tqdm import tqdm
regex = "(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])"

input_folder = "input"

output_folder = "output"
output_path = f"https://jetsimon.com/cts-media/public/"

errors = []

count = 0

files = os.listdir(input_folder)

seen = {}

for filename in tqdm(files):

    count += 1
    if(filename.startswith(".") or filename == "MODLOADERFILE.html"):
        continue

    #print(f"SCRAPING MOD ({count}/{len(files)}): {filename}")

    f = open(input_folder + "/" + filename, "r", encoding="utf8")
    contents = f.read()

    opener = urllib.request.URLopener()
    opener.addheader('User-Agent', 'whatever')

    index = 0
    for match in re.findall(regex, contents):
        url = ""
        for chunk in match:
            if(chunk in {'https', 'http'}):
                chunk = chunk + "://"
            url += chunk

        if(url[-1] == "/"):
            url = url[:len(url) - 1]

        path = urlparse(url).path
        ext = os.path.splitext(path)[1]

        if "discord" not in url.lower():
            #print(f"{url} is not a discord url so no worries")
            continue

        if(ext == ""):
            #print("Will not download [" + url + "] because no ext")
            continue

        if(ext in {".html", ".htm", ".php", ".m4a", ".mp3", ".wav"}):
            #print("Will not download [" + url + "] because forbidden extension " + ext)
            continue
            
        fname = filename.replace(".html", "") + "_" + str(index) + ext

        if url in seen:
            #print(f"Already saw url [{url}] so skipping download and replacing with [{seen[url]}]")
            contents = contents.replace(url, seen[url])
            continue

        #print(f"Trying to download from [{url}] as [{fname}]")
        try:
            opener.retrieve(url, "output/" + fname)
            contents = contents.replace(url, output_path + fname)
            seen[url] = output_path + fname
        except Exception as e:
            err = f"Error downloading url [{url}] for mod [{filename}]: {e}"
            print(err)
            errors.append(err)
        
        index += 1

    f.close()
    f = open(input_folder + "/" + filename, "w", encoding="utf8")
    f.write(contents)
    f.close()

f = open("errs.txt", "w", encoding="utf8")

f.write(f"-- Errors ({len(errors)}) --\n" + "\n".join(errors))
f.close()