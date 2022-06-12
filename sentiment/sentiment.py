import pandas as pd
import csv
from reddit_scraper.reddit import api_scraper, start_epoch, end_epoch
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

reddit_df = api_scraper(start_epoch, end_epoch)
analyzer = SentimentIntensityAnalyzer()

def sentiment_analyzis(reddit_df):
    reddit_df['time'] = reddit_df['created_utc'].dt.year * 10000 + reddit_df['created_utc'].dt.month * 100 + reddit_df['created_utc'].dt.day
    reddit_df['sentiment'] = reddit_df['body'].apply(lambda x: analyzer.polarity_scores(x))
    reddit_df['sentiment_score'] = reddit_df['sentiment'].apply(lambda x: x['compound'])
    id_df = reddit_df.groupby(['time'])['id'].count()
    score_df = reddit_df.groupby(['time'])['sentiment_score'].mean()
    reddit_df = id_df.to_frame().merge(score_df.to_frame(), on = 'time')
    return reddit_df

if __name__ == '__main__':
    analyzed_df = sentiment_analyzis(reddit_df)
    analyzed_df.to_csv(r'C:\Users\suchy\Downloads\bitcoin_analyzis.csv')
    # bitcoin_data = pd.read_csv('Bitcoin.csv')
