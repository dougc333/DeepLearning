import os,sys
import tweepy
#import twitter
from pathlib import Path
import spacy
from ehtan import Config
from pymongo import MongoClient

class Download_Data:
	def __init__(self):
		self.client = MongoClient()
		self.db = self.client['twitter']
		c = Config.Config()
		self.consumer_key = c.consumer_key
		self.consumer_secret = c.consumer_secret
		self.access_token= c.access_token
		self.access_secret= c.access_secret
		self.authentication = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		self.authentication.set_access_token(self.access_token, self.access_secret)
		self.api = tweepy.API(self.authentication)
		self.nlp = spacy.load('en')
		self.user_name = 'jeremyphoward'
		self.user_names = {'jeremyhoward':db['jeremyhoward'],'mwseibel':db['mwseibel'],'bramcohen':db['bramcohen']}


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
		elif(os.path.exists(self.linux)):
			print('linux server')
			self.path = '/home/dc/twitter_nlp/'
		else:
			print('system error no paths are available')
			return
		#for all user names
		for x in self.user_names.keys():
			self.save_file = Path(self.path+x+".txt")
			print('self.save_file:',self.save_file)
			if self.save_file.is_file() == False:
				open(self.save_file, 'a').close()
			fh = open(self.save_file, 'a')
			self.user_names[x] = fh

	def test_create_dirs(self):
		'''
		#error check print out file handles for all user_names
		:return:
		'''
		for x in self.user_names.keys():
			print(self.user_names[x])


	def save_data(self):
		for x in self.user_names:
			print('user:',x)
			mongo_coll = user_names[x]
			new_tweets = self.api.user_timeline(screen_name =x ,count=10)
			for tweet in new_tweets:
				print(tweet.text)
				mongo_coll.insert(tweet._json)
				print(tweet.retweet_count, tweet.favorite_count)
				self.user_names[x].write("{},{},{},{}\n".format(tweet.id,tweet.text,tweet.retweet_count, tweet.favorite_count))
				print('-----------------------')
				doc = self.nlp(tweet.text)
				for entity in doc.ents:
					print("tweet id:", tweet.id)
					print(entity.text, entity.label_)
			self.user_names[x].close()

	def is_question(s):
		if "?" in s:
			return True
		return False

if __name__=='__main__':
	d = Download_Data()
	d.create_dirs()
	d.save_data()


