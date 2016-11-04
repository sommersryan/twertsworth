import compose, tweet, vision, urllib.request, markovify, random
from config import CORPUS_URL, ENCODING

req = urllib.request.Request(CORPUS_URL)
with urllib.request.urlopen(req) as corpusSource:
	textModel = markovify.Text(corpusSource.read().decode(ENCODING))

sourceReplies = [tweet.getMediaURL(a) for a in tweet.checkReplies()] #this should be a list of tuples with the ID of each reply and the URLs of the media in them

for reply in sourceReplies:
	random.shuffle(reply[1]) #pick a rando image
	imageLabels = vision.getLabels(reply[1][0])
	
	tweetText = compose.writePoem(textModel,imageLabels[:2])
	tweet.replyTo(tweetText,reply[0]) #does reply ID need to be string or int hmmm
	