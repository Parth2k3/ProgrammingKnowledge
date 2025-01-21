import boto3

Polly = boto3.client('polly')

text = "Hello, my name is Polly. I am a text-to-speech service."

response = Polly.synthesize_speech(
    Text = text,
    OutputFormat = 'mp3',
    VoiceId = 'Joanna'
)

with open('output.mp3', 'wb') as f:
    f.write(response['AudioStream'].read())

print("Audio file saved as output.mp3")