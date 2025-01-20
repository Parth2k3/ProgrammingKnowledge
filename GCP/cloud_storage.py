from google.cloud import storage

storage_client = storage.Client.from_service_account_json("storage_key.json")

bucket = storage_client.get_bucket("test-bucket-qwe")

# blob = bucket.blob('car.jpg')

# blob.upload_from_filename('car.jpg')
# print('uploaded!!')

blobs = bucket.list_blobs()
for blob in blobs:
    print(blob.name)
from datetime import timedelta
url = blob.generate_signed_url(expiration=timedelta(minutes=1), method='GET')
print(url)