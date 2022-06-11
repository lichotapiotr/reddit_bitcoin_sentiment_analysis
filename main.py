from reddit_scraper.reddit import scraper, start_epoch, end_epoch

if __name__ == '__main__':
    reddit_df=scraper(start_epoch, end_epoch)