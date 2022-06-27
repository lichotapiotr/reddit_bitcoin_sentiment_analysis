import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# from reddit_scraper.reddit import api_scraper, start_epoch, end_epoch
# from sentiment.sentiment import sentiment_analyzis

if __name__ == '__main__':
    # reddit_df = api_scraper(start_epoch, end_epoch)
    # analyzed_df = sentiment_analyzis(reddit_df)

    analyzed_df = pd.read_csv(r'C:\Users\suchy\Downloads\bitcoin_analyzis.csv')
    bitcoin_df = pd.read_csv(r'C:\Users\suchy\Downloads\Bitcoin.csv')

    analyzed_df = analyzed_df.drop([0, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163])

    analyzed_df['time'] = pd.to_datetime(analyzed_df['time'], format='%Y%m%d', errors='ignore')
    # analyzed_df.plot(x='time', y='sentiment_score', kind='line')

    print(analyzed_df['sentiment_score'].describe())
    analyzed_df['sentiment_score'] = analyzed_df['sentiment_score']*300000

    bitcoin_df['Data'] = pd.to_datetime(bitcoin_df['Data'], format='%d.%m.%Y', errors='ignore')
    bitcoin_df['Data'] = bitcoin_df['Data'].dt.strftime('%Y%m%d')
    bitcoin_df['Data'] = pd.to_datetime(bitcoin_df['Data'], format='%Y%m%d', errors='ignore')

    bitcoin_df['Otwarcie'] = bitcoin_df['Otwarcie'].str.replace('.', '', regex=True)
    bitcoin_df['Otwarcie'] = bitcoin_df['Otwarcie'].str.replace(',', '.', regex=True)
    bitcoin_df['Otwarcie'] = bitcoin_df['Otwarcie'].astype('str').astype('float')

    ax = bitcoin_df.plot(x='Data', y='Otwarcie', color='r', kind='line')
    analyzed_df.plot(ax=ax, x='time', y='sentiment_score', kind='line')
    plt.show()

    bitcoin_df['time'] = bitcoin_df['Data']
    correlation_df = analyzed_df.merge(bitcoin_df[['time', 'Otwarcie']], on='time')
    sentiment_array = correlation_df['sentiment_score'].to_numpy()
    opening_array = correlation_df['Otwarcie'].to_numpy()
    pearson = np.corrcoef(sentiment_array, opening_array)

    print(pearson)
    print(bitcoin_df['Otwarcie'].describe())

    bitcoin_df = bitcoin_df.set_index('Data')
    bitcoin_df = bitcoin_df.shift(periods=3)
    bitcoin_df = bitcoin_df.reset_index()

    ax = bitcoin_df.plot(x='Data', y='Otwarcie', color='r', kind='line')
    analyzed_df.plot(ax=ax, x='time', y='sentiment_score', kind='line')
    plt.show()

    correlation_df = analyzed_df.merge(bitcoin_df[['time', 'Otwarcie']], on='time')
    sentiment_array = correlation_df['sentiment_score'].to_numpy()
    opening_array = correlation_df['Otwarcie'].to_numpy()
    pearson = np.corrcoef(sentiment_array, opening_array)

    print(pearson)

    print(stats.spearmanr(sentiment_array, opening_array))


