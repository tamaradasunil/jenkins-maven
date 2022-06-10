

import logging
import boto3
from botocore.exceptions import ClientError

# Retrieve the list of existing buckets
s3 = boto3.resource('s3', aws_access_key_id='AKIA6LQSYPWOAZDZTOMC',
 aws_secret_access_key='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')


for bucket in s3.buckets.all():
    print (bucket.name)
    
	
s3 = boto3.resource('s3',
 aws_access_key_id='AKIA6LQSYPWOAZDZTOMC',
 aws_secret_access_key='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'
 #aws_session_token='if session token',
 )
size_byte=0
my_bucket=s3.Bucket('allbuckets')
for my_bucket_object in my_bucket.objects.all():
 print(my_bucket_object.key)
 size_byte=size_byte+my_bucket_object.size
totalsize_gb=size_byte/1000/1024/1024
print(size_byte)
print(totalsize_GB)


