import json, base64, urllib.request
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

def getImageContent(imageURL):
	req = urllib.request.Request(imageURL)
	with urllib.request.urlopen(req) as response:
		return base64.b64encode(response.read())
	
def buildRequest(image, content=True):
	if content: 
		imageRequest = {'content' : image.decode('UTF-8')}
	else:
		imageRequest = {'source': {'gcsImageUri':image}}
		
	request = json.dumps(
				{'requests':[
								{
									'features':
									[
										{
											'type':'label_detection'
										}
									],
									'image': imageRequest
								}
							]
				})
	return request

