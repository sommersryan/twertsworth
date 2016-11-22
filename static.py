from boto.s3.connection import S3Connection
from boto.s3.key import Key
from config import S3_BUCKET

storageConnection = S3Connection()
datastore = storageConnection.get_bucket(S3_BUCKET)

def getSinceID():
	return datastore.get_key('since_id').get_contents_as_string()

def setSinceID(newID):
	datastore.get_key('since_id').set_contents_from_string(newID)
	return True
	
def resetSinceID():
	datastore.get_key('since_id').set_contents_from_string('779688396516012032')
	return True
	
def getGoogleCredentials():
	return datastore.get_key('google_credentials').get_contents_as_string()