import os,sys
import tweepy
#import twitter
from pathlib import Path
import spacy

class Download_Data:
	def __init__(self):
		self.consumer_key = 'eFIaiOuxsny01VVQ2QWISK1Mw'
		self.consumer_secret = 'gDQI5EiCMJJaaNI8XVNhfZXwuCOYfeJ3XsOUNHvsXqgq0Hoj9T'
		self.access_token='76976448-Otz8w4yMKx6yCEWTH3dNTfuF8LYeLgqdoDrcl0oBK'
		self.access_secret='NFPFe2EzuKWuzRKmY1RENUBfQzGeGbAS1JzjX3Eu3GwDE'
		self.authentication = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		self.authentication.set_access_token(self.access_token, self.access_secret)
		self.api = tweepy.API(self.authentication)
		self.nlp = spacy.load('en')
		self.save_file = Path('/home/dc/ethan/howard.txt')
		self.user_name = 'jeremyphoward'
		if self.save_file.is_file()==False:
			open('/home/dc/ethan/howard.txt','a').close()
		self.fh = open(self.save_file,'a')

	def save_data(self):
		new_tweets = self.api.user_timeline(screen_name ='jeremyphoward' ,count=200)
		for tweet in new_tweets:
			print(tweet.text)
			self.fh.write(tweet.text)
			print('-----------------------')
			doc = self.nlp(tweet.text)
			for entity in doc.ents:
				print("tweet id:", tweet.id)
				print(entity.text, entity.label_)
		self.fh.close()

	def is_question(s):
		if "?" in s:
            		return True
		return False

if __name__=='__main__':
	d = Download_Data()
	d.save_data()


