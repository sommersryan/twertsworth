from boto.s3.connection import S3Connection
from boto.s3.key import Key

storageConnection = S3Connection()
datastore = storageConnection.get_bucket('twertsworth')

def getSinceID():
	return datastore.get_key('since_id').get_contents_as_string()

def setSinceID(newID):
	datastore.get_key('since_id').set_contents_from_string(newID)
	return True
	
def resetSinceID():
	datastore.get_key('since_id').set_contents_from_string('779688396516012032')
	return True