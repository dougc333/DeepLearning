import os, sys
import tweepy
# import twitter
from pathlib import Path
import spacy
import Config
import json
from clean import Clean

#add mock object for testing..test API downloading messages in groups of 10
# from pymongo import MongoClient
# to get this to run correctly, remove dougc333/min.txt, dougc333/max.txt

class Download_Data:
    def __init__(self):
        # self.client = MongoClient()
        # self.db = self.client['twitter']
        c = Config.Config()
        self.consumer_key = c.consumer_key
        self.consumer_secret = c.consumer_secret
        self.access_token = c.access_token
        self.access_secret = c.access_secret
        self.authentication = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.authentication.set_access_token(self.access_token, self.access_secret)
        self.api = tweepy.API(self.authentication)
        self.nlp = spacy.load('en')
        self.user_name = 'jeremyphoward'
        # self.user_names = {'jeremyhoward': db['jeremyhoward'], 'mwseibel': db['mwseibel'], 'bramcohen': db['bramcohen']}
        #self.user_names = {'jeremyhoward', 'mwseibel', 'bramcohen'}
        self.user_names = {'dougc333'}
        self.tweet_ids = []
        self.removeFiles()

    def removeFiles(self):
        for user in self.user_names:
            if os.path.exists(os.path.join(os.getcwd(),user,"min.txt")):
                os.remove(os.path.join(os.getcwd(),user,"min.txt"))
            if os.path.exists(os.path.join(os.getcwd(), user, "max.txt")):
                os.remove(os.path.join(os.getcwd(), user, "max.txt"))

    def create_dirs(self):
        '''
        /home/dc/ethan/howard.txt
        :param file_name:
        :return:
        '''
        self.macOS = '/Users/dc/DeepLearning/twitter_nlp/'
        self.linux = '/home/dc/twitter_nlp/'

        if os.path.exists(self.macOS):
            print('macOS')
            self.path = '/Users/dc/DeepLearning/twitter_nlp/'
        elif (os.path.exists(self.linux)):
            print('linux server')
            self.path = '/home/dc/twitter_nlp/'
        else:
            print('system error no paths are available')
            return
        # for all user names open up a file handle and store it in a dict for each user. This is crappy design
        # cant remember there is an open file handle here
        for x in self.user_names:
            if os.path.exists(self.path + "/" + x):
                # do nothing
                print()
            else:
                os.mkdir(self.path + "/" + x)

    def test_dir(self,user):
        """
        test what we get by min max of dir files is same as what we see from download. Should be different
        :param user: user name directory. Directory should alreaay exist.
        :return:nothing, print statements
        """
        clean = Clean(user)


    def find_minmax(self, user,list_id):
        print("len list_id:{}".format(len(list_id)))
        if len(list_id)==0:
            return
        list_id.sort()
        print("min_sort:{} max_sort:{}".format(list_id[0], list_id[len(list_id)-1]))
        #data = {"user":user, "min":list_id[0], "max":list_id[len(list_id)-1]}
        #json_data = json.dumps(data)
        #print (json_data)
        m = self.min_max(list_id[0],list_id[len(list_id)-1],user,self.path)
        m.save_to_file()

    def save_list(self,tweet_list):
        with open("list_tweetids.txt", "w") as fh:
            for x in tweet_list:
                fh.write(x)
                fh.write("\n")
            fh.close()

    def save_data(self):
        list_id = []
        list_json = []
        for x in self.user_names:
            print('user:', x)
            # mongo_coll = user_names[x]
            if(os.path.exists(self.path+x+"/max.txt" and self.path+x+"/min.txt"))==True:
                since_id_fh = open(self.path+x+"/max.txt")
                max_id_fh = open(self.path+x+"/min.txt")
                since_id = since_id_fh.read()
                max_id = max_id_fh.read()
                new_tweets = self.api.home_timeline(screen_name=x, since_id = since_id, count=10)
            else:
                #need to make dir
                new_tweets = self.api.home_timeline(screen_name=x, count=10)
            for tweet in new_tweets:
                print(tweet.text)

                self.save_json(x, tweet._json, tweet.id)
                list_json.append(tweet._json)
                list_id.append(tweet.id)
                # mongo_coll.insert(tweet._json)
                # print(tweet.retweet_count, tweet.favorite_count)
                # self.user_names[x].write(
                #    "{},{},{},{}\n".format(tweet.id, tweet.text, tweet.retweet_count, tweet.favorite_count))
                # print('-----------------------')
                doc = self.nlp(tweet.text)
                for entity in doc.ents:
                    print("tweet id:", tweet.id)
                    self.tweet_ids.append(tweet.id)
                    # print(entity.text, entity.label_)
            # ipdb.set_trace()
            self.find_minmax(x,list_id)
            clean = Clean(x)

    def save_json(self, user, json_data, tweet_id):
        with open(self.path + "/" + user + "/" + str(tweet_id) + user, "w") as fh:
            fh.write(str(json_data))
            fh.write("\n")
            fh.write("\n")
        fh.close()

    class min_max:
        def __init__(self,min,max,user,path):
            self.min = min
            self.max = max
            self.user=user
            self.path=path

        def save_to_file(self):
            with open(self.path+self.user+"/min.txt","w") as fh:
                fh.write(str(self.min))
            fh.close()
            with open(self.path  + self.user + "/max.txt","w") as fh:
                fh.write(str(self.max))
            fh.close()

if __name__ == '__main__':
    d = Download_Data()
    d.create_dirs()
    d.save_data()
    print("done")
