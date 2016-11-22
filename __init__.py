import compose, tweet, static, urllib.request, markovify, random, logging, time, sys, vision, httplib2
from config import CORPUS_URL, ENCODING, SOURCE_FREQUENCY, SCOPES, API_DISCOVERY_FILE
from oauth2client.service_account import ServiceAccountCredentials

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

req = urllib.request.Request(CORPUS_URL)

with urllib.request.urlopen(req) as corpusSource:
	textModel = markovify.Text(corpusSource.read().decode(ENCODING))
	
while True:

	with open('google_credentials','wb') as credentialsFile:
		credentialsFile.write(static.getGoogleCredentials())
		credentials = ServiceAccountCredentials.from_json_keyfile_name(
		'google_credentials', SCOPES)
	
	http = httplib2.Http()

	service = discovery.build('vision', 'v1', http, discoveryServiceUrl=API_DISCOVERY_FILE, credentials=credentials)

	logging.info("Service built successfully.")

	newReplies = tweet.checkReplies()
	mediaReplies = []

	#Just take the replies with pictures

	for reply in newReplies: 
		if reply.media:
			mediaReplies.append(reply)
			
	if random.randint(1,720) <= SOURCE_FREQUENCY:
		mediaReplies.append(tweet.getSourceTweet())

	#Make list of tuples with the necessary info for each reply
		
	toDoList = [tweet.getMediaURL(a) for a in mediaReplies] 
	logging.info('Processing replies %s'," ".join([r[0] for r in toDoList]))

	for reply in toDoList:

		random.shuffle(reply[2])
		logging.info('Using image %s for reply %s',reply[2][0],reply[0])
		imageLabels = vision.getLabels(reply[2][0], service)
		logging.info('Using labels %s',','.join(imageLabels))
		tweetText = compose.writePoem(textModel, imageLabels, reply[1])
		tweet.replyTo(tweetText, int(reply[0])) #Reply ID needs to be int
		if int(static.getSinceID()) < int(reply[0]):
			static.setSinceID(reply[0])
	time.sleep(60)
