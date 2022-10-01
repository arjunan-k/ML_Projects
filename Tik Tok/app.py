import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

hashtag = st.text_input("Search for a hashtag here", value="")

st.sidebar.markdown(
    "<div><img src='https://raw.githubusercontent.com/arjunan-k/ML_Projects/"
    "main/TikTok/data/logo.webp?token=GHSAT0AAAAAABYLGBKO2GQFIN2PYFGW3IL4YZX46GQ' width=80 />"
    "<h1 style='display:inline-block'>Tiktok Analytics</h1></div>",
    unsafe_allow_html=True)
st.sidebar.markdown("Hello There")
st.sidebar.markdown(
    "To get <ol><li>Enter the <i>hashtag</i> you wish to analyse</li> <li>Hit <i>"
    "Get Data</i>.</li> <li>Get analyzing</li></ol>",
    unsafe_allow_html=True)

# Button
if st.button("Get Data"):
    df = pd.read_csv("tiktokdata.csv")

    fig = px.histogram(df, x="desc", y="stats_diggCount", height=300)
    st.plotly_chart(fig, use_container_width=True)

    left_col, right_col = st.columns(2)
    scatter1 = px.scatter(df,
                          x="stats_shareCount",
                          y="stats_commentCount",
                          size='stats_playCount',
                          color='stats_playCount',
                          hover_data=["desc"])
    left_col.plotly_chart(scatter1, use_container_width=True)
    right_col.plotly_chart(scatter1, use_container_width=True)
    df