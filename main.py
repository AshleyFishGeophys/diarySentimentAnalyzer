import streamlit as st
import plotly.express as px
from sentiment import analyze_diary_journals

dates, pos_scores, neg_scores = analyze_diary_journals()

st.title("Diary Tone")

st.subheader("Positivity")
fig_pos = px.line(x=dates, y=pos_scores, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(fig_pos)

st.subheader("Negativity")
fig_neg = px.line(x=dates, y=neg_scores, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(fig_neg)
