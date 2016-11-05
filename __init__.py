import compose, tweet, static, urllib.request, markovify, random, logging
from config import CORPUS_URL, ENCODING

logging.basicConfig(filename='runtime.log', level=logging.DEBUG)

req = urllib.request.Request(CORPUS_URL)
with urllib.request.urlopen(req) as corpusSource:
	textModel = markovify.Text(corpusSource.read().decode(ENCODING))
	
with open('tmp/google_credentials','wb') as credentialsFile:
	credentialsFile.write(static.getGoogleCredentials())
	
import vision

newReplies = tweet.checkReplies()
mediaReplies = []

#Just take the replies with pictures

for reply in newReplies: 
	if reply.media:
		mediaReplies.append(reply)

#Make list of tuples with the necessary info for each reply
		
toDoList = [tweet.getMediaURL(a) for a in mediaReplies] 
logging.info('Processing replies %s'," ".join([r[0] for r in toDoList]))

for reply in toDoList:

	#Going to randomize the order and just pick the first one
	
	random.shuffle(reply[2])
	logging.info('Using image %s for reply %s',reply[2][0],reply[0])
	imageLabels = vision.getLabels(reply[2][0])
	logging.info('Using labels %s',','.join(imageLabels[:2]))
	tweetText = compose.writePoem(textModel,imageLabels[:2],reply[1])
	tweetCharList = list(tweetText)
	tweetCharList[0] = tweetCharList[0].upper()
	finalCharList = [w.replace(',','\r') for w in tweetCharList]
	finalTweet = "".join(finalCharList)
	tweet.replyTo(finalTweet,int(reply[0])) #Reply ID needs to be int
	