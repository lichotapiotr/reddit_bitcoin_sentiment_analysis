from psaw import PushshiftAPI
import pandas as pd
import datetime as dt


api = PushshiftAPI()

start_epoch = int(dt.datetime(2022, 1, 1).timestamp())
end_epoch = int(dt.datetime(2022, 6, 1).timestamp())

def api_scraper(start_epoch, end_epoch):
    api_request_generator = api.search_comments(subreddit='Bitcoin', after=start_epoch, before=end_epoch, filter=['author', 'created_utc', 'title', 'body', 'score', 'id'])
    df_reddit = pd.DataFrame([comment.d_ for comment in api_request_generator])
    df_reddit['created_utc'] = pd.to_datetime(df_reddit['created_utc'], utc=True, unit='s')
    return df_reddit

#api_request_generator = api.search_submissions(subreddit='Bitcoin', limit=1000, after=start_epoch, before=end_epoch)
#df_reddit = pd.DataFrame([submission.d_ for submission in api_request_generator])
#df_reddit = df_reddit[['author', 'author_flair_css_class', 'created_utc', 'id', 'num_comments', 'score', 'selftext', 'title', 'upvote_ratio']]

if __name__ == '__main__':
    reddit_df = api_scraper(start_epoch, end_epoch)