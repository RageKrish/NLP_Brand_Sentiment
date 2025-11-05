import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from newsapi import NewsApiClient
import praw
from dotenv import load_dotenv
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load environment variables
load_dotenv()

# Initialize APIs
newsapi = NewsApiClient(api_key=os.getenv("NEWSAPI_KEY"))
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

analyzer = SentimentIntensityAnalyzer()

# Streamlit UI
st.title("🧠 NLP Brand Sentiment Analyzer")
brand = st.text_input("Enter a brand name (e.g., Flipkart, Apple, Tesla):")

def collect_brand_data(brand_name, news_limit=10, reddit_limit=10):
    data = []
    # NewsAPI
    news = newsapi.get_everything(q=brand_name, language='en', page_size=news_limit)
    for article in news['articles']:
        data.append({'source': 'news', 'text': article.get('title', '') + " " + str(article.get('description', ''))})
    # Reddit
    for submission in reddit.subreddit("all").search(brand_name, limit=reddit_limit, time_filter='month'):
        data.append({'source': 'reddit', 'text': submission.title + " " + submission.selftext})
    return pd.DataFrame(data)

def get_sentiment(text):
    score = analyzer.polarity_scores(text)
    if score['compound'] >= 0.05:
        return 'Positive'
    elif score['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

if brand:
    st.write(f"🔎 Collecting sentiment data for **{brand}** ...")
    df = collect_brand_data(brand)
    df['sentiment'] = df['text'].apply(get_sentiment)

    st.subheader("Sentiment Summary")
    st.write(df['sentiment'].value_counts())

    # Bar chart
    st.bar_chart(df['sentiment'].value_counts())

    # WordCloud
    st.subheader("Word Cloud")
    text = " ".join(df['text'])
    wc = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)
