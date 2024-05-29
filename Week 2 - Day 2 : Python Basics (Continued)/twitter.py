import os
import csv

base_dir = os.path.dirname(__file__)

class Account:
    def __init__(self, csvfile):
        self.handle = csvfile[:-4]
        self.bio = ''
        self._tweets = []
        with open( os.path.join(base_dir, csvfile), 'r',encoding='utf-8') as file:
          reader = csv.reader(file)
          first_row = 1
          for row in reader:
            if first_row == 1:
              self.bio = row[-1]
              first_row = 0
            self._tweets.append(Tweet(row))
    def __getitem__(self,index):
      return self._tweets[index]
    def __len__(self):
      return len(self._tweets)
    def filter(self, term):
      self._tweets = [tweet for tweet in self._tweets if term.lower() in tweet.text.lower()]
    def inv_filter(self, term):
      self._tweets = [tweet for tweet in self._tweets if term.lower() not in tweet.text.lower()]

class Tweet:
    def __init__(self,tweet):
        self.text = tweet[0]
        self.likes = int(tweet[1])
        self.retweets = int(tweet[2])
        self.date_time = tweet[3]