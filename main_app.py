import streamlit as st
import app1
import app2

st.set_page_config(
    page_title="All-in-One Music AI App",
    layout="wide"
)

st.sidebar.title("📌 Navigation")

page = st.sidebar.radio(
    "Go to",
    ["🎵 Music Generator", "⚙️ Model Settings"]
)

if page == "🎵 Music Generator":
    app1.run()

elif page == "⚙️ Model Settings":
    app2.run()
