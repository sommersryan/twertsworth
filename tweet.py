import config
import twitter
import os

api = twitter.Api(
					consumer_key = config.CONSUMER_KEY,
					consumer_secret = config.CONSUMER_SECRET,
					access_token_key = config.ACCESS_TOKEN,
					access_token_secret = config.ACCESS_SECRET
				)
				
def post(tweet):
	if len(tweet) > 140:
		#Shorten the tweet to fit character limit
		tweet = tweet[:140]
	api.PostUpdate(tweet)
	return "Tweeted " + tweet 

def checkReplies():
	lastReply = os.environ.get("LASTREPLY") or '792210713766924288' #arbitrary sinceId for an old tweet
	replies = api.GetMentions(since_id = lastReply)
	if replies: 
		os.environ["LASTREPLY"] = replies[-1].id_str
	return replies
	
def getMediaURL(status):
	mediaURLs = [pic.AsDict()["media_url"] for pic in status.media]
	return tuple(status,mediaURLS)

	