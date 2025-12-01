import streamlit as st
import pandas as pd
from scraping import scrape_sec_filings, scrape_crunchbase
from ai_analysis import summarize_article, extract_entities, categorize_article

# Title
st.title("Market Intelligence Prototype")

# Sidebar filters
st.sidebar.header("Filters")
industry = st.sidebar.selectbox("Industry", ["Aerospace & Defense", "Transportation & Mobility", "PLM"])
source = st.sidebar.selectbox("Data Source", ["SEC Filings", "Crunchbase"])

# Scrape data
if source == "SEC Filings":
    data = scrape_sec_filings(ticker="AAPL")
else:
    data = scrape_crunchbase(query="PLM")

# Display data
st.header(f"Recent {source} for {industry}")
for item in data:
    st.subheader(item["title"])
    st.write(f"**Date:** {item['date']}")
    st.write(f"**Description:** {item['description']}")

    # AI Analysis
    if st.button(f"Analyze: {item['title']}"):
        summary = summarize_article(item["description"])
        entities = extract_entities(item["description"])
        category = categorize_article(item["description"])

        st.write("---")
        st.write("### AI Analysis")
        st.write(f"**Summary:** {summary}")
        st.write(f"**Category:** {category}")
        st.write("**Entities:**")
        for entity in entities:
            st.write(f"- {entity['text']} ({entity['label']})")
        st.write("---")
