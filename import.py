# Import helper
# Takes a twitter export (~2022 format, unsure if changed)
# Gets relevent information and media, exports into a jekyll consumable format. 

from pathlib import Path
import json
import sys
from datetime import datetime

if len(sys.argv) == 1: 
    raise ValueError("import.py PATH_TO_EXPORT_FOLDER")

TWITTER_EXPORT = Path(sys.argv[1])

print(f"Import from {TWITTER_EXPORT}")

twitter_data_file = TWITTER_EXPORT / "data/tweets.js"

json_data = []

with open(twitter_data_file) as f: 
    datafile = f.read().replace("window.YTD.tweets.part0 = ","")

    json_data = json.loads(datafile)

for tweet in json_data: 
    t = tweet["tweet"]
    
    # Only export media tweets

    if "media" not in t["entities"].keys(): 
        continue

    t_text = t["full_text"]

    m = t["entities"]["media"][0] # from my data, only single media
    ext = m["media_url"].split("/")[-1]
    _id = m["id"]
    t_media = _id + "-" + ext
    t_created_at = t["created_at"]

    format_string = "%a %b %d %H:%M:%S %z %Y"

    # Parsing the date string into a datetime object
    t_date = datetime.strptime(t_created_at, format_string)

    print(t_date)
    print(t_text)
    print(t["favorite_count"], t["retweet_count"])
    print(f"\tdata/tweets_media/{t_media}")
    print("")
