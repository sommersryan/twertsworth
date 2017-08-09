import os

#Twitter Keys
#Set the following variables in your environment or fill them in here with the values from your twitter application at apps.twitter.com
CONSUMER_KEY = os.environ.get("CONSUMER_KEY") or ''
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET") or ''
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN") or ''
ACCESS_SECRET = os.environ.get("ACCESS_SECRET") or ''

CORPUS_URL = os.environ.get("CORPUS_URL") or ''

MAX_CHAR = 140 #the tweeter's burden

ENCODING = 'UTF-8' #encoding of your corpus file, mine is from Gutenberg ebooks so it's UTF-8

#s3 keys for static storage with Heroku 
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID") or ''
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY") or ''
S3_BUCKET = os.environ.get("S3_BUCKET") or ''

SOURCE_ACCOUNTS = ['archillect','GettyImages','AP_Images','blessediimages','NASAGoddardPix','GettyArchive'] #accounts to pull pictures from
SOURCE_FREQUENCY = 0 #avg times per 12 hours to pick a source tweet to reply to 

API_DISCOVERY_FILE = 'https://vision.googleapis.com/$discovery/rest?version=v1'
SCOPES = ['https://www.googleapis.com/auth/cloud-platform']

#list of words to exclude from model keys
EXCLUDE_WORDS = ['person']
