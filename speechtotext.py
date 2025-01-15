from google.cloud import speech_v1 as speech
import os
from pydub import AudioSegment
import wave

with wave.open("sample_audio.wav", "rb") as wav_file:
    sample_rate = wav_file.getframerate()
    print(f"Sample rate: {sample_rate}")

client = speech.SpeechClient.from_service_account_file('gcp_key.json')

def convert_to_mono(ipnut_file, output_file):
    audio = AudioSegment.from_file(ipnut_file)
    audio = audio.set_channels(1)
    audio.export(output_file, format="wav")
    print('Converted to mono')

def transcribe_audio(input_file):
    with open(input_file, 'rb') as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz = sample_rate,
            language_code = 'en-US'
        )
        response = client.recognize(config=config, audio=audio)
        for result in response.results:
            print(f'Transcript: {result.alternatives[0].transcript}')
            print(f'Confidence: {result.alternatives[0].confidence}')
    return response

convert_to_mono("sample_audio.wav", "audio_sample_mono.wav")
transcribe_audio("audio_sample_mono.wav")