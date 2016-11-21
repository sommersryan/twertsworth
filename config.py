import os

#Twitter Keys
#Set the following variables in your environment or fill them in here with the values from your twitter application at apps.twitter.com
CONSUMER_KEY = os.environ.get("CONSUMER_KEY") or ''
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET") or ''
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN") or ''
ACCESS_SECRET = os.environ.get("ACCESS_SECRET") or ''

CORPUS_URL = os.environ.get("CORPUS_URL") or ''

MIN_CHAR = 70 #really short tweets are boring
MAX_CHAR = 140 #the tweeter's burden
ATTEMPTS = 10 #number of times we'll try to make a suitable tweet for each model key

ENCODING = 'UTF-8' #encoding of your corpus file, mine is from Gutenberg ebooks so it's UTF-8

#s3 keys for static storage with Heroku 
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID") or ''
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY") or ''

SOURCE_ACCOUNTS = ['archillect','GettyImages','AP_Images'] #accounts to pull pictures from
SOURCE_FREQUENCY = 3 #avg times per 12 hours to pick a source tweet to reply to 