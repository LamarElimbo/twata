import tweepy

DATA = 'data/master.csv'
STOPWORDS_DIR = 'data/stopwords.txt'
STOPWORDS = []

TRACK_TERMS = ['bbuk', 'bigbrother', 'bb2017']
CONNECTION_STRING = "sqlite:///bbTweets.db"
CSV_NAME = "bbTweets.csv"
TABLE_NAME = "bbTweets"

NEG_CONTESTANTS = {'arthur': 0, 'chanelle': 0, 'charlotte': 0, 'deborah': 0, 'ellie': 0, 'hannah': 0, 'imran': 0, 'kayleigh': 0, 'kieran': 0, 'lotan': 0, 'mandy': 0, 'raph': 0, 'rebecca': 0, 'sukhvinder': 0, 'tom': 0}

POS_CONTESTANTS = {'arthur': 0, 'chanelle': 0, 'charlotte': 0, 'deborah': 0, 'ellie': 0, 'hannah': 0, 'imran': 0, 'kayleigh': 0, 'kieran': 0, 'lotan': 0, 'mandy': 0, 'raph': 0, 'rebecca': 0, 'sukhvinder': 0, 'tom': 0}

# ---------- Commands to run simultaneously in the terminal ----------
	#change to streaming directory
    #bokeh serve --allow-websocket-origin=www.lamartalkscode.com
    #python vizzer.py
    #python tweetStreamer.py
    
    
{"Amelia":0, "Brandi":0, "Chad":0, "Derek":0, "Helen":0, "Jemma":0, "Jordan":0, "Karthik":0, "Marissa":0, "Paul":0, "Sam":0, "Sandi":0, "Sarah":0, "Shaun":0, "Trisha":0}