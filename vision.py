import json, base64, urllib.request, static, os, logging
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'google_credentials' #this allows get_application_default

logging.info("Credential file location added.")

credentials = GoogleCredentials.get_application_default()

logging.info("Credentials retrieved.")

service = discovery.build('vision', 'v1', credentials=credentials)

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
		
		response = service_request.execute()
		
		logging.info("Request executed successfully.")
		
		try:
			labels = [label['description'] for label in response['responses'][0]['labelAnnotations']] #heard u liked list comprehensions 
			logging.info("Labels retrieved: %s",",".join[a for a in labels])
		except KeyError:
			labels = [' ',' '] #return a blank list if Google can't find any labels
			logging.info("No labels acquired, returning blanks.")
		return labels