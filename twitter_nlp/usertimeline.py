import Config
import tweepy
import os
import json
import time
import sys

class UserTimeline:

    def __init__(self,user_name, user_dir):
        c = Config.Config()
        self.consumer_key = c.consumer_key
        self.consumer_secret = c.consumer_secret
        self.access_token = c.access_token
        self.access_secret = c.access_secret
        self.authentication = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.authentication.set_access_token(self.access_token, self.access_secret)
        self.api = tweepy.API(self.authentication)
        self.user_name = user_name
        self.user_dir = user_dir

        self.path = "/Users/dc/DeepLearning/twitter_nlp/" + self.user_dir
        if os.path.isdir(self.path)==False:
            os.makedirs(self.path)

        self.last_id_file ="last_id.txt"
        self.first = "first.txt"
        self.last_tweet_id = None


    def get_tweets(self):
        if (os.path.exists(os.path.join(self.path, self.last_id_file))):
            with open(os.path.join(self.path,self.last_id_file),"r") as read_fh:
                self.last_read = int(read_fh.read().strip())
            read_fh.close()
            with open(os.path.join(self.path,self.first),"r") as read_fh:
                self.highest_read = int(read_fh.read().strip())
            read_fh.close()

            print("last_read:{}".format(self.last_read))
            print("highest_read:{}".format(self.highest_read))
            print(self.user_name)
            print(self.last_read)
        if(os.path.exists(os.path.join(self.path,self.last_id_file))):
            new_tweets = self.api.user_timeline(screen_name=self.user_name,count=20,max_id=self.last_read,text_mode="Extended")
        else:
            new_tweets = self.api.user_timeline(screen_name=self.user_name, count=20, text_mode="Extended")
            with open(os.path.join(self.path,self.first),"w") as first_fh:
                first_fh.write(str(new_tweets[0].id))
            first_fh.close()
        print(len(new_tweets))
        last_id = new_tweets[len(new_tweets)-1].id #integer
        with open(os.path.join(self.path,self.last_id_file),"w") as last_fh:
            last_fh.write(str(last_id))
        last_fh.close()

        for tweet in new_tweets:
            print(tweet.id,tweet.text)
            with open(os.path.join(self.path,str(tweet.id)),"w") as fh:
                fh.write(json.dumps(tweet._json))
            fh.close()

    def is_last_tweet(self,tweet):
        """
        compare if the most recent tweet is the same as the last one. if so then we are stuck
        :param tweet:
        :return:
        """
        if self.last_tweet_id == None:
            self.last_tweet_id = tweet.id
        elif (tweet.id == self.last_tweet.id):
            print("last tweet!!")
            sys.exit()
        else:
            self.last_tweet_id = tweet.id

if __name__=="__main__":
    u = UserTimeline('@mwseibel','mw_tweets')
    for i in range(300):
        u.get_tweets()
        time.sleep(10)

