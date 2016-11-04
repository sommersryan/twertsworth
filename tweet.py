import config, twitter, os, logging

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
	logging.info('Obtained statuses: %s',','.join([reply.id_str for reply in replies]))
	return replies
	
def getMediaURL(status):
	mediaURLs = [pic.AsDict()["media_url"] for pic in status.media]
	logging.info('Obtained %s URLs',str(len(mediaURLs)))
	replyPrefix = '@' + status.user.screen_name + '\r'
	return (status.id_str, replyPrefix, mediaURLs) #return the ID of what's going to be replied to, a prefix that's the @ and linebreak, and list of media URLs

def replyTo(tweet,replyToID):
	api.PostUpdate(status=tweet,in_reply_to_status_id=replyToID)
	return "Reply complete"