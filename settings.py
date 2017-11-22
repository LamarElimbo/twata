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
X_CATEGORIES = {'cat1': 0, 'cat2': 0}

NEG_COUNTS = X_CATEGORIES

POS_COUNTS = X_CATEGORIES