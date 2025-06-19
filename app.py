import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")


st.title("📈 Stock Market Dashboard")

powerbi_url = "https://app.powerbi.com/reportEmbed?reportId=0691052d-692f-4af7-943f-5e1b2b5e0f6c&autoAuth=true&embeddedDemo=true"

# Inject full-width CSS and embed iframe
components.html(
    f"""
    <style>
        .report-container {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            border: none;
            margin: 0;
            padding: 0;
            overflow: hidden;
            z-index: 999999;
        }}
    </style>
    <iframe class="report-container"
        src="{powerbi_url}"
        allowFullScreen="true">
    </iframe>
    """,
    width=1000,
    height=550,
    scrolling=False,
)