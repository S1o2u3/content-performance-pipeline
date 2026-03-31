import requests
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")

CHANNELS = [
    "UCBcRF18a7Qf58cCRy5xuWwQ",
    "UCnUYZLuoy1rq1aVMwx4aTzw",
    "UCVHdiIjxT0TYSMOq0-xYCXQ",
    "UC-8QAzbLcRglXeN_MY9blyw",
    "UCddiUEpeqJcYeBxX1IVBKvQ",
    "UCJXGnMr6J0gLd1cDKoxynxQ",
    "UCeiYXex_fwgYDonaTcSIk6w",
    "UCq-Fj5jknLsUf-MWSy4_brA",
    "UCbmNph6atAoGfqLoCL_duAg",
    "UC0RhatS1pyxInC00YKjjBqQ",
    "UCsvn_Po0SmunchJYtttggZg",
    "UCnUYZLuoy1rq1aVMwx4aTzw",
    "UCXuqSBlHAE6Xw-yeJA0Tunw",
    "UCsooa4yRKGN_zEE8iknghZA",
    "UC9-y-6csu5WGm29I7JiwpnA",
    "UCHnyfMqiRRG1u-2MsSQLbXA",
    "UCiGm_E4ZwYSHV3bcW1pnSeQ",
    "UCbmNph6atAoGfqLoCL_duAg",
    "UC295-Dw4tzbAdAmzeox8_Aw",
    "UCnUYZLuoy1rq1aVMwx4aTzw",
    "UCdC0An4ZPNr_YiFiYoVbwaw",
    "UC0RhatS1pyxInC00YKjjBqQ",
    "UCJXGnMr6J0gLd1cDKoxynxQ",
    "UCVHdiIjxT0TYSMOq0-xYCXQ",
    "UC8butISFwT-Wl7EV0hUK0BQ",
    "UCo8bcnLyZH8tBIH9V1mLgqQ",
    "UCnUYZLuoy1rq1aVMwx4aTzw",
    "UCddiUEpeqJcYeBxX1IVBKvQ",
    "UC3yT9Gh_CzjKh4HZLPAVP-A",
    "UCGbshXdMAvBrGFEEBNI_0YA"
]
def fetch_videos(channel_id):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "key": API_KEY,
        "channelId": channel_id,
        "part": "snippet",
        "type": "video",
        "maxResults": 50
    }
    response = requests.get(url, params=params).json()
    return response.get("items", [])

def save_videos(videos):
    conn = sqlite3.connect("pipeline.db")
    cursor = conn.cursor()
    count = 0
    for item in videos:
        if item["id"].get("videoId"):
            cursor.execute("""
                INSERT OR IGNORE INTO videos
                (video_id, channel_id, title, publish_date)
                VALUES (?, ?, ?, ?)
            """, (
                item["id"]["videoId"],
                item["snippet"]["channelId"],
                item["snippet"]["title"],
                item["snippet"]["publishedAt"]
            ))
            count += 1
    conn.commit()
    conn.close()
    return count

total = 0
for channel_id in CHANNELS:
    videos = fetch_videos(channel_id)
    count = save_videos(videos)
    total += count
    print(f"Channel {channel_id}: saved {count} videos")

print(f"Total videos in database: {total}")