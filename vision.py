import json, base64, urllib.request, static, os, logging
from googleapiclient import discovery

def getLabels(imageURL, service):
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