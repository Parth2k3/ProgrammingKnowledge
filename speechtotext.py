from google.cloud import speech_v1 as speech
from pydub import AudioSegment

# Load the audio file
audio = AudioSegment.from_file("sample_audio.wav")

# Convert to mono
audio = audio.set_channels(1)

# Export the converted audio
audio.export("audio_sample_mono.wav", format="wav")

client = speech.SpeechClient.from_service_account_file("gcp_key.json")

with open("audio_sample_mono.wav", "rb") as audio_file:
    content = audio_file.read()

# Configure audio and recognition settings
audio = speech.RecognitionAudio(content=content)
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    language_code="en-US"
)

# Perform recognition
response = client.recognize(config=config, audio=audio)

# Print the transcription
for result in response.results:
    print("Transcript:", result.alternatives[0].transcript)
