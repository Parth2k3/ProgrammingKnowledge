from google.cloud import language_v1

# Authenticate using the service account key file
client = language_v1.LanguageServiceClient.from_service_account_json("gcp_key.json")

# Input text to analyze
text_content = "Google Cloud Platform is amazing for building scalable applications!"

# Document object
document = language_v1.Document(content=text_content, type_=language_v1.Document.Type.PLAIN_TEXT)

# Analyze sentiment
response = client.analyze_sentiment(request={'document': document})
sentiment = response.document_sentiment

# Output the sentiment score and magnitude
print("Sentiment Analysis Results:")
print(f" - Score: {sentiment.score}")
print(f" - Magnitude: {sentiment.magnitude}")

response = client.analyze_entities(request={'document': document})
print("Entities Found:")
for entity in response.entities:
    print(f" - {entity.name} ({language_v1.Entity.Type(entity.type_).name})")

