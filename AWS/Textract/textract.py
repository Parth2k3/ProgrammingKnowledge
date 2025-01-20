# Combine all functionality into one script
import boto3

textract = boto3.client('textract')

# Load local document
with open('ocr.jpeg', 'rb') as doc_file:
    doc_bytes = doc_file.read()

response = textract.analyze_document(
    Document={'Bytes': doc_bytes},
    FeatureTypes=['FORMS', 'TABLES']
)

# Print text
print("Extracted text:")
for block in response['Blocks']:
    if block['BlockType'] == 'LINE':
        print(block['Text'])

# Print key-value pairs
print("\nKey-Value Pairs:")
for block in response['Blocks']:
    if block['BlockType'] == 'KEY_VALUE_SET':
        print(f"{block.get('Text', 'N/A')}")

print("\nTables:")
for block in response['Blocks']:
    if block['BlockType'] == 'TABLE':
        print(f"Table detected: {block}")