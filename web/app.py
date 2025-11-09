import streamlit as st
from web.pages import home, diagnosis, dashboard

PAGES = {
    "Home": home,
    "Diagnosis": diagnosis,
    "Dashboard": dashboard
}

st.set_page_config(page_title="AI-VetStreamX", layout="wide")

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page.app()