import streamlit as st

def app():
    st.title("AI-VetStreamX 🐾")
    st.image("web/static/logo.png", width=300)
    st.markdown("""
    ระบบผู้ช่วยวินิจฉัยโรคผิวหนังสัตว์เลี้ยงเบื้องต้นด้วยปัญญาประดิษฐ์
    - ฟรีสำหรับผู้ใช้
    - สร้างโดยนักเรียนมัธยม
    """)
    if st.button("เริ่มวิเคราะห์โรค"):
        st.experimental_rerun()