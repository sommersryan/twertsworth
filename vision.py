import json, base64, urllib.request, static, os
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'tmp/google_credentials' #this allows get_application_default

credentials = GoogleCredentials.get_application_default()
service = discovery.build('vision', 'v1', credentials=credentials)

def getLabels(imageURL):
	req = urllib.request.Request(imageURL)
	with urllib.request.urlopen(req) as response:
		image_content = base64.b64encode(response.read())
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
		response = service_request.execute()
		try:
			labels = [label['description'] for label in response['responses'][0]['labelAnnotations']] #heard u liked list comprehensions 
		except KeyError:
			labels = [' ',' '] #return a blank list if Google can't find any labels
		return labels