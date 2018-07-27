import Config
import tweepy
import json
class UserLimits:
    def __init__(self):
        c = Config.Config()
        self.consumer_key = c.consumer_key
        self.consumer_secret = c.consumer_secret
        self.access_token = c.access_token
        self.access_secret = c.access_secret
        self.authentication = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.authentication.set_access_token(self.access_token, self.access_secret)
        self.api = tweepy.API(self.authentication)
        resp = self.api.rate_limit_status()
        print(resp)
        print("--------------------------------")
        print(type(resp))
        print(resp['rate_limit_context'])
        print("list statuses limit:",resp['resources']['lists']['/lists/statuses']['limit'])
        print("list statuses remaining",resp['resources']['lists']['/lists/statuses']['remaining'])

        print("rate limit requests quota:{}".format(resp['resources']['application']['/application/rate_limit_status']['limit']))
        print("rate limit requests left:{}".format(resp['resources']['application']['/application/rate_limit_status']['remaining']))
        print("time:",resp['resources']['application']['/application/rate_limit_status']['reset'])

        print(resp['resources']['statuses']['/statuses/user_timeline']['limit'])
        print(resp['resources']['statuses']['/statuses/user_timeline']['remaining'])

if __name__=="__main__":
    u = UserLimits()
