from boto.s3.connection import S3Connection
from boto.s3.key import Key

storageConnection = S3Connection()
datastore = storageConnection.get_bucket('twertsworth')
since_id = datastore.get_key('since_id').get_contents_as_string()
