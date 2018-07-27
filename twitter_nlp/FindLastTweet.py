import os

class FindLastTweet:
    def __init__(self):
        self.path = "/Users/dc/DeepLearning/twitter_nlp/jh_tweets/"
        self.list_files = [x for x in os.listdir(self.path) if os.path.isfile(os.path.join(self.path,x))]
        self.list_files.remove("first.txt")
        self.list_files.remove("last_id.txt")
        self.list_files.sort()
        #convert to int for sorting. doesnt matter; sorts same w/string type
        self.list_files = [int(x) for x in self.list_files]
        print(len(self.list_files))
        print(self.list_files[0],self.list_files[len(self.list_files)-1])
        #print(type(self.list_files[0]))
        #for x in self.list_files:
        #    if x==996469720583827457: #verified this is in last_id.txt
        #        print("found:{}".format(x))

if __name__=="__main__":
    f = FindLastTweet()
