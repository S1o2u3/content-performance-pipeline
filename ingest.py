import requests
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("AIzaSyCLKgZjXnKZHL3Hte8W0jbr-IpAEbpyv7w")

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
    "UC0RhatS1pyxInC00YKjjBqQ"
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