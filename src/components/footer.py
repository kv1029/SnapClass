import streamlit as st

def footer_home():
    logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center;">
            <p style="margin:0; color:white;">Created with by</p>
            <img src="{logo_url}" style="max-height:25px;" />
            <p style="margin:0; color:white; font-weight:bold;">Apna College</p>
        </div>
    """, unsafe_allow_html=True)