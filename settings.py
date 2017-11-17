import tweepy

DATA = 'data/master.csv'
STOPWORDS_DIR = 'data/stopwords.txt'
STOPWORDS = []

# What terms on Twitter would you like to track?
TRACK_TERMS = []

CONNECTION_STRING = "sqlite:///trackedTweets.db"
CSV_NAME = "trackedTweets.csv"
TABLE_NAME = "trackedTweets"

# What are the values in this topic that you want to compare
NEG_TOPICS = {'arthur': 0, 'chanelle': 0, 'charlotte': 0, 'deborah': 0, 'ellie': 0, 'hannah': 0, 'imran': 0, 'kayleigh': 0, 'kieran': 0, 'lotan': 0, 'mandy': 0, 'raph': 0, 'rebecca': 0, 'sukhvinder': 0, 'tom': 0}

POS_TOPICS = {'arthur': 0, 'chanelle': 0, 'charlotte': 0, 'deborah': 0, 'ellie': 0, 'hannah': 0, 'imran': 0, 'kayleigh': 0, 'kieran': 0, 'lotan': 0, 'mandy': 0, 'raph': 0, 'rebecca': 0, 'sukhvinder': 0, 'tom': 0}