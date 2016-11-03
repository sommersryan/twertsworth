import os

#Twitter Keys
#Set the following variables in your environment or fill them in here with the values from your twitter application at apps.twitter.com
CONSUMER_KEY = os.environ.get("CONSUMER_KEY") or ''
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET") or ''
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN") or ''
ACCESS_SECRET = os.environ.get("ACCESS_SECRET") or ''

MIN_CHAR = 80 #really short tweets are boring
MAX_CHAR = 140 #the tweeter's burden
ATTEMPTS = 10 #number of times we'll try to make a suitable tweet for each model key

ENCODING = 'UTF-8' #encoding of your corpus file, mine is from Gutenberg ebooks so it's UTF-8