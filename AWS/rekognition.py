import boto3
rekognition = boto3.client('rekognition', region_name='us-east-1')

with open('car.jpg', 'rb') as image:
    image_bytes = image.read()

response = rekognition.detect_labels(
    Image = {'Bytes': image_bytes},
    MaxLabels = 10
)

print('Detected objects:')
for label in response['Labels']:
    print(f'{label["Name"]} ({label["Confidence"]:.2f}%)')

with open('ocr.png', 'rb') as image:
    image_bytes = image.read()

response = rekognition.detect_text(
    Image = {'Bytes': image_bytes}
)
print('\nDetected text:')
for text in response['TextDetections']:
    print(text['DetectedText'], ' - ', 'Confidence: ', text['Confidence'])

with open('portrait.jpeg', 'rb') as image:
    image_bytes = image.read()

response = rekognition.detect_faces(
    Image = {'Bytes': image_bytes},
    Attributes = ['ALL']
)

for face in response['FaceDetails']:
    print('\nDetected face:')
    print(f" - Emotions: {face['Emotions']}")
    print(face['Gender']['Value'])
    print(face['Confidence'])
    print(face['AgeRange'])