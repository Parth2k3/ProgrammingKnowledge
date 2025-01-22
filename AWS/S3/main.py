import boto3
s3 = boto3.client('s3')

bucket_name = 'test-bucket-123whg'
# s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})

# print('bucket is created')

file_name = 'car.jpg'
# s3.upload_file(file_name, bucket_name, file_name)
# print('file is uploaded')

# s3.download_file(bucket_name, file_name, 'downloaded-car.jpg')
# print('file downloaded')

response = s3.list_objects_v2(Bucket = bucket_name)
if 'Contents' in response:
    for obj in response['Contents']:
        print(obj['Key'])
