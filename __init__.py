import compose, tweet, vision, static, urllib.request, markovify, random, logging
from config import CORPUS_URL, ENCODING

logging.basicConfig(filename='runtime.log', level=logging.DEBUG)

req = urllib.request.Request(CORPUS_URL)
with urllib.request.urlopen(req) as corpusSource:
	textModel = markovify.Text(corpusSource.read().decode(ENCODING))
	
with open('tmp/google_credentials','w') as credentialsFile:
	credentialsFile.write(static.getGoogleCredentials())

newReplies = tweet.checkReplies()
mediaReplies = []

for reply in newReplies: #just take the replies with pictures
	if reply.media:
		mediaReplies.append(reply)

toDoList = [tweet.getMediaURL(a) for a in mediaReplies] #make list of tuples with the necessary info for each reply
logging.info('Processing replies %s'," ".join([r[0] for r in toDoList]))

for reply in toDoList:
	random.shuffle(reply[2]) #going to randomize the order and just pick the first one
	logging.info('Using image %s for reply %s',reply[2][0],reply[0])
	imageLabels = vision.getLabels(reply[2][0])
	logging.info('Using labels %s',','.join(imageLabels[:2]))
	tweetText = compose.writePoem(textModel,imageLabels[:2],reply[1])
	tweet.replyTo(tweetText,int(reply[0])) #reply ID needs to be int
	