# cts-scraper
Simple python script to scrape CTS mods for media to keep backups

If you want to use this to scrape files from a bunch of html files with links in them:

1. Create folder called input in the same directory as the python script. Put all the html files in it.
2. Create an empty folder called output.
3. Run the script. It will log any errors in a file called errs.txt.
4. All html files in input will be modified to use the link format supplied in the python script.
5. All media scraped will be in output.
