import boto
import boto.s3.connection
access_key = 'AKIA6LQSYPWOAZDZTOMC'
secret_key = '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'
conn = boto.connect_s3( aws_access_key_id = access_key, aws_secret_access_key = secret_key)
for bucket in conn.get_all_buckets():
	total_bytes = 0
	name = bucket.name
	for key in bucket:
		total_bytes += key.size
	total_bytes = total_bytes/1024/1024/1024
	print ("Bucket Name:" ,name, "Size: ",total_bytes ,"GB")
