# cts-scraper
Simple python script to scrape CTS mods for media to keep backups

If you want to use this to scrape files from a bunch of html files with links in them:

1. Create folder called input in the same directory as the python script. Put all the html files in it.
2. Create an empty folder called output.
3. Run the script. It will log any errors in a file called errs.txt.
4. All html files in input will be modified to use the link format supplied in the python script.
5. All media scraped will be in output.

Things to modify:

Right now the path for URLs is set to 

output_folder = "mod_media"
output_path = f"../../../../../static/{output_folder}/"

This is because on CTS I have it so image files are stored in the static/mod_media folder. Switch those as you need. 

The

```
ext in {".html", ".htm", ".mp3", ".mp4", ".wav", ".php", ".m4a"}
```

section causes it to NOT download files with those extensions. Remove or add extensions as suits your needs.
