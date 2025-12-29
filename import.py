# Import helper
# Takes a twitter export (~2022 format, unsure if changed)
# Gets relevent information and media, exports into a jekyll consumable format.

from pathlib import Path
import json
import sys
from datetime import datetime
from textwrap import dedent
import shutil
import re

if len(sys.argv) == 1:
    raise ValueError("import.py PATH_TO_EXPORT_FOLDER")

TWITTER_EXPORT = Path(sys.argv[1].strip())

print(f"Import from {TWITTER_EXPORT}")

twitter_data_file = TWITTER_EXPORT / "data/tweets.js"

json_data = []
landing_media = Path("img")

with open(twitter_data_file) as f:
    datafile = f.read().replace("window.YTD.tweets.part0 = ", "")

    json_data = json.loads(datafile)

for tweet in json_data:
    t = tweet["tweet"]

    # Only export media tweets
    if "media" not in t["entities"].keys():
        continue

    # Ignore video (not in my data apart from meme posts)
    if "/video/" in t["entities"]["media"][0]["expanded_url"]: 
        continue

    # Ignore any retweets (fuzzy)
    if t["full_text"].startswith("RT @"):
        continue

    url_pattern = re.compile(r"https?://\S+|www\.\S+")

    t_text = url_pattern.sub("", t["full_text"])

    t_original_url = re.findall(r"https?://t.co/\S+", t["full_text"])[0]

    m = t["entities"]["media"][0]  # from my data, only single media items exist.
    ext = m["media_url"].split("/")[-1]
    t_media = t["id"] + "-" + ext
    t_created_at = t["created_at"]

    format_string = "%a %b %d %H:%M:%S %z %Y"

    # Parsing the date string into a datetime object
    t_date = datetime.strptime(t_created_at, format_string)

    print(t_date)
    print(t_text)
    print(t["favorite_count"], t["retweet_count"])
    media_file = f"data/tweets_media/{t_media}"
    print("")

    post_name = f"{t_date.strftime('%Y-%m-%d')}-{t['id']}.md"

    shutil.copy(TWITTER_EXPORT / media_file, landing_media / t_media)

    post = dedent(
        f"""\
        ---
        layout: tweet
        title: {t['id']}
        date: {t_date}
        media: /img/{t_media}
        original_url: {t_original_url}
        retweets: {t['retweet_count']}
        favorites: {t["favorite_count"]}
        ---
        """
    ).strip()
    post += f"\n\n{t_text}"

    with open(f"_posts/{post_name}", "w") as f:
        f.write(post)
