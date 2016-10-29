import json, base64, urllib.request
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

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
		labels = [label['description'] for label in response['responses'][0]['labelAnnotations']]
		return labels