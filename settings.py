import tweepy

DATA = 'data/master.csv'
STOPWORDS_DIR = 'data/stopwords.txt'
STOPWORDS = []

# What terms on Twitter would you like to track?
TRACK_TERMS = ['toronto', 'new york', 'miami']

CONNECTION_STRING = "sqlite:///trackedTweets.db"
CSV_NAME = "trackedTweets.csv"
TABLE_NAME = "trackedTweets"

# What are the values in this topic that you want to compare
X_CATEGORIES = {'toronto': 0, 'new york': 0, 'miami':0}

NEG_COUNTS = X_CATEGORIES

POS_COUNTS = X_CATEGORIES