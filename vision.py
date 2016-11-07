import json, base64, urllib.request, static, os, logging, httplib2
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

API_DISCOVERY_FILE = 'https://vision.googleapis.com/$discovery/rest?version=v1'
http = httplib2.Http()


logging.info("Credential file location added.")

credentials = GoogleCredentials.get_application_default()

logging.info("Credentials retrieved.")

service = discovery.build('vision', 'v1', http, discoveryServiceUrl=API_DISCOVERY_FILE, credentials=credentials)

logging.info("Service built successfully.")

def getLabels(imageURL):
	req = urllib.request.Request(imageURL)
	with urllib.request.urlopen(req) as response:
		image_content = base64.b64encode(response.read())
		
		logging.info("Image stream retrieved.")
		
		service_request = service.images().annotate(body={
			'requests':[
								{
									'image':
										{
											'content': image_content.decode('UTF-8')
										},
									'features':
										[
											{
												'type':'label_detection'
											}
										]}
							]})
							
		logging.info("Request built.")
		
		response = service_request.execute(num_retries=5)
		
		logging.info("Request executed successfully.")
		
		try:
			labels = [label['description'] for label in response['responses'][0]['labelAnnotations']] #heard u liked list comprehensions 
			logging.info("Labels retrieved: %s",','.join([a for a in labels]))
		except KeyError:
			labels = [' ',' '] #return a blank list if Google can't find any labels
			logging.info("No labels acquired, returning blanks.")
		return labels