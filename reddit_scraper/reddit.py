from psaw import PushshiftAPI
import pandas as pd
import datetime as dt
import numpy as np

api = PushshiftAPI()

start_epoch = int(dt.datetime(2022, 1, 1).timestamp())
end_epoch = int(dt.datetime(2022, 5, 31).timestamp())


def scraper(start_epoch, end_epoch):
    api_request_generator = api.search_submissions(subreddit='Bitcoin', limit=1000, after=start_epoch, before=end_epoch)
    df_reddit = pd.DataFrame([submission.d_ for submission in api_request_generator])
    df_reddit = df_reddit[['author', 'author_flair_css_class', 'created_utc', 'id', 'num_comments', 'score', 'selftext', 'title', 'upvote_ratio']]
    return df_reddit


if __name__ == '__main__':
    reddit_df = scraper(start_epoch, end_epoch)
    print(reddit_df)
