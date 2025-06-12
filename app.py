import streamlit as st
import streamlit.components.v1 as components

st.title("📈 Stock Market Dashboard")

powerbi_url = "https://app.powerbi.com/reportEmbed?reportId=0691052d-692f-4af7-943f-5e1b2b5e0f6c&autoAuth=true&embeddedDemo=true"

components.html(
    f"""
    <iframe title="Stock Market Dashboard"
            width="100%" 
            height="450"
            src="{powerbi_url}"
            frameborder="0"
            allowfullscreen="true">
    </iframe>
    """,
    height=470,  # Set slightly more than iframe height
    scrolling=True
)
