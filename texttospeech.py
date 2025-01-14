
from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient.from_service_account_file("gcp_key.json")

input_text = texttospeech.SynthesisInput(text="Hello, Welcome to google cloud")

voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
)

audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

response = client.synthesize_speech(input=input_text, voice=voice, audio_config=audio_config)

with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')