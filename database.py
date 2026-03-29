import sqlite3

conn = sqlite3.connect("pipeline.db")
cursor = conn.cursor()

cursor.executescript("""
    CREATE TABLE IF NOT EXISTS videos (
        video_id TEXT PRIMARY KEY,
        channel_id TEXT,
        title TEXT,
        publish_date TEXT,
        duration TEXT,
        tags TEXT
    );

    CREATE TABLE IF NOT EXISTS metrics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        video_id TEXT,
        date TEXT,
        views INTEGER,
        watch_time_min REAL,
        ctr REAL,
        likes INTEGER,
        comments INTEGER
    );

    CREATE TABLE IF NOT EXISTS ai_insights (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        video_id TEXT,
        generated_at TEXT,
        topic_cluster TEXT,
        seo_score INTEGER,
        recommendation TEXT
    );

    CREATE TABLE IF NOT EXISTS trends (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        keyword TEXT,
        date TEXT,
        interest_score INTEGER
    );
""")

conn.commit()
conn.close()
print("Done! 4 tables created.")