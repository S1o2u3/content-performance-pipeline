from groq import Groq
import sqlite3
import os
import time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

conn = sqlite3.connect("pipeline.db")
cursor = conn.cursor()

videos = cursor.execute(
    "SELECT video_id, title FROM videos LIMIT 500"
).fetchall()

for video_id, title in videos:
    prompt = f"""
    You are a content strategy expert.
    Video title: "{title}"
    
    Reply with exactly 3 lines:
    Topic: one word category
    SEO Score: number out of 100
    Recommendation: one sentence suggestion
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    cursor.execute("""
        INSERT INTO ai_insights
        (video_id, generated_at, recommendation)
        VALUES (?, ?, ?)
    """, (video_id, datetime.now().isoformat(), response.choices[0].message.content))

    print(f"Done: {title}")
    time.sleep(2)

conn.commit()
conn.close()
print("All insights saved!")