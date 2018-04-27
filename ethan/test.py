from pathlib import Path
import spacy

class Download_Data:
    def __init__(self):
        self.nlp = spacy.load('en')
        self.save_file = Path('/Users/dc/ethan/howard.txt')
        self.user_name = 'jeremyphoward'
        if self.save_file.is_file()==False:
            open('/Users/dc/ethan/howard.txt','a').close()
        self.fh = open(self.save_file,'w+')
        
    def save_data(self):
        new_tweets = api.user_timeline(screen_name ='jeremyphoward' ,count=200)
        for tweet in new_tweets:
            print(tweet.text)
            self.fh.write(tweet.text)
            print('-----------------------')
            doc = nlp(tweet.text)
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
    
