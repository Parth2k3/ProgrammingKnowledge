from google.cloud import storage

# Initialize the storage client
storage_client = storage.Client.from_service_account_json('cloud_key.json')

# Specify the bucket
bucket = storage_client.get_bucket('test-bucket-qyd')

# Specify the file to upload
blob = bucket.blob('car.jpg')

# # Upload the file
# blob.upload_from_filename('car.jpg')
# print("File uploaded successfully!")

blobs = bucket.list_blobs()
for blob in blobs:
    print(blob.name)

from datetime import timedelta
url = blob.generate_signed_url(expiration=timedelta(minutes=1), method='GET')
print(f'Signed URL: {url}')
