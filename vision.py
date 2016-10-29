import json

def buildRequest(image):
	request = json.dumps(
				{'requests':[
								{
									'features':
									[
										{
											'type':'label_detection'
										}
									],
									'image':
									{
										'source':
										{
											'gcsImageUri':image
										}
									}
								}
							]
				})
	return request
