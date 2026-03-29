import streamlit as st
import sqlite3
import pandas as pd

st.title("Content Performance Intelligence Pipeline")

conn = sqlite3.connect("pipeline.db")

st.subheader("Videos Collected")
videos = pd.read_sql("SELECT * FROM videos", conn)
st.dataframe(videos)

st.subheader("AI Recommendations")
insights = pd.read_sql("""
    SELECT v.title, a.recommendation, a.generated_at
    FROM ai_insights a
    JOIN videos v ON a.video_id = v.video_id
""", conn)
st.dataframe(insights)

st.download_button(
    label="Export Partner Report",
    data=insights.to_csv(index=False),
    file_name="partner_report.csv"
)

conn.close()