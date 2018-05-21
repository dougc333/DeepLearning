import tweepy
import Config




class Twitter_Download:
    """
    runs as cron job
    downlooads json data
    """
    def __init__(self):
        self.consumer_key = Config.consumer_key