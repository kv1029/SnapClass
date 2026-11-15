import streamlit as st


def footer_home():
    st.markdown("""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
        <p style="font-weight:bold; color:white; margin:0;"> Created with ❤️ by <span style="font-weight:900; letter-spacing:1px;">KV</span> </p>  
        </div>
                
                """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
        <p style="font-weight:bold; color:black; margin:0;"> Created with ❤️ by <span style="font-weight:900; color:#5865F2; letter-spacing:1px;">KV</span> </p>  
        </div>
                
                """, unsafe_allow_html=True)
