from google.cloud import translate_v2 as translate

# Authenticate using the service account key file
client = translate.Client.from_service_account_json("gcp_key.json")

# Text to translate
text = "Hello, how are you?"

# Translate text to Spanish (es)
result = client.translate(text, target_language="es")

# Print the translated text
print(f"Original text: {text}")
print(f"Translated text: {result['translatedText']}")
result = client.detect_language(result['translatedText'])
print(f"Detected language: {result['language']}")
