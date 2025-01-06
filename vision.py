from google.cloud import vision
import io

# Authenticate using the service account key file
client = vision.ImageAnnotatorClient.from_service_account_json("gcp_key.json")

# Path to the image file
image_path = "car.jpg"

# Load the image
with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

# Create an image object
image = vision.Image(content=content)

# Perform label detection
response = client.label_detection(image=image)
labels = response.label_annotations

# Print detected labels
print("Labels detected:")
for label in labels:
    print(f"- {label.description} (Score: {label.score})")

ocr_image_path = "ocr.png"
with io.open(ocr_image_path, 'rb') as image_file:
    content = image_file.read()

# Create an image object
image = vision.Image(content=content)
response = client.text_detection(image=image)
texts = response.text_annotations
print(texts)
for text in texts:
    print(f"Detected text: {text.description}")
