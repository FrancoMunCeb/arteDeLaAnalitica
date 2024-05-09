import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt


df = pd.read_csv('covid19_tweets.csv')


analyzer = SentimentIntensityAnalyzer()


def classify_sentiment(text):
    if not isinstance(text, str):
        return 'neutral'
    scores = analyzer.polarity_scores(text)
    if scores['compound'] >= 0.05:
        return 'positive'
    elif scores['compound'] <= -0.05:
        return 'negative'
    else:
        return 'neutral'


df['date'] = pd.to_datetime(df['date'], errors='coerce')


mask_tweets = df[df['text'].str.contains('Wearamask', case=False, na=False)]


mask_tweets['sentiment'] = mask_tweets['text'].apply(classify_sentiment)


mask_tweets_filtered = mask_tweets[mask_tweets['sentiment'] != 'neutral']


daily_sentiment = mask_tweets_filtered.groupby([mask_tweets_filtered['date'].dt.date, 'sentiment']).size().unstack(fill_value=0)


daily_sentiment[['positive', 'negative']].plot(kind='line', figsize=(10, 6), title='Evolution of Positive and Negative Sentiment about Wearing a Mask Over Time')
plt.ylabel('Number of Tweets')
plt.xlabel('Date')
plt.show()
