from google.cloud import texttospeech

# Set up client
client = texttospeech.TextToSpeechClient.from_service_account_file("gcp_key.json")

# Define input text
ssml_text = """
<speak>
  Hello! This is <prosody pitch="+2st">a higher pitch</prosody>,
  and this is <prosody rate="slow">spoken slowly</prosody>.
  <break time="500ms"/> Thank you for listening!
</speak>
"""

input_text = texttospeech.SynthesisInput(ssml=ssml_text)

# Define voice configuration
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", 
    ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# Define audio configuration
audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

# Perform text-to-speech request
response = client.synthesize_speech(input=input_text, voice=voice, audio_config=audio_config)

# Save the audio to a file
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print("Audio content written to file 'output.mp3'")
