# 🎯 Content Performance Intelligence Pipeline

> Transform raw video data into actionable content strategy using AI — automatically.

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python)
![SQLite](https://img.shields.io/badge/SQLite-Database-green?style=flat-square&logo=sqlite)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?style=flat-square&logo=streamlit)
![LLM](https://img.shields.io/badge/LLM-Powered-purple?style=flat-square)

---

## 📌 What This Does

Most content teams drown in raw metrics but starve for insight. This pipeline fixes that.

It automatically:
- 📥 **Ingests** video metadata and performance data from a public REST API
- 🗄️ **Stores** everything in a clean, normalized SQL schema
- 🤖 **Analyzes** each video using an LLM — topic, SEO score, optimization tip
- 📊 **Surfaces** findings in an interactive dashboard with one-click report export

---

## 🏗️ Architecture
```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐     ┌───────────────┐
│  REST API   │────▶│   Python     │────▶│   SQLite    │────▶│   Streamlit   │
│  (Videos)   │     │  Ingestion   │     │  Database   │     │   Dashboard   │
└─────────────┘     └──────────────┘     └──────┬──────┘     └───────────────┘
                                                 │
                                         ┌───────▼──────┐
                                         │   LLM API    │
                                         │ (Insights)   │
                                         └──────────────┘
```

---

## 🗄️ Database Schema
```sql
videos       → video_id, channel_id, title, publish_date, duration, tags
metrics      → video_id, date, views, watch_time_min, ctr, likes, comments
ai_insights  → video_id, generated_at, topic_cluster, seo_score, recommendation
trends       → keyword, date, interest_score
```

> Raw metrics and AI-generated insights are stored in **separate tables** — so you can rerun, version, and compare AI recommendations without ever touching source data.

---

## 📊 Dashboard Preview

![Dashboard](screenshots/dashboard.png)

---

## ⚙️ How to Run

**1. Clone the repo**
```bash
git clone https://github.com/S1o2u3/content-performance-pipeline.git
cd content-performance-pipeline
```

**2. Install dependencies**
```bash
pip install requests groq streamlit pandas python-dotenv
```

**3. Create a `.env` file**
```
YOUTUBE_API_KEY=your_key_here
GROQ_API_KEY=your_key_here
```

**4. Run the pipeline**
```bash
python3 database.py       # create tables
python3 ingest.py         # fetch videos
python3 ai_insights.py    # generate AI recommendations
streamlit run dashboard.py # launch dashboard
```

---

## 💡 Key Design Decisions

| Decision | Why |
|---|---|
| Separate `ai_insights` table | Allows independent versioning of AI output |
| `INSERT OR IGNORE` in ingestion | Prevents duplicates on re-runs |
| LLM output stored as text | Keeps schema flexible as prompts evolve |
| Streamlit for dashboard | Fastest path from SQL query to visual output |

---

## 🚀 Built With

| Tool | Purpose |
|---|---|
| Python | Pipeline orchestration and API calls |
| SQLite | Local SQL database |
| REST API | Video metadata collection |
| Groq LLM API | Topic clustering and title optimization |
| Streamlit | Interactive dashboard |
| python-dotenv | Secure API key management |