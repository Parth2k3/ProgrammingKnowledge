s3_uri = "s3://aud-bucket/sample_audio.wav"
import boto3

transcribe = boto3.client('transcribe')

def start_transcription_job():
    transcription_job_name = "sample-job-2"
    response = transcribe.start_transcription_job(
        TranscriptionJobName = transcription_job_name,
        Media = {'MediaFileUri': s3_uri},
        MediaFormat = 'wav',
        LanguageCode='en-US'
    )
    return transcription_job_name

def wait_for_transcription_job(transcription_job_name):
    while True:
        response = transcribe.get_transcription_job(
            TranscriptionJobName = transcription_job_name
        )
        status = response['TranscriptionJob']['TranscriptionJobStatus']
        if status in ['COMPLETED', 'FAILED']:
            print('status : ', status)
            if status == 'COMPLETED':
                print('transcription completed')
                return response['TranscriptionJob']['Transcript']['TranscriptFileUri']
            else:
                print('the job failed')

# job_name = start_transcription_job()
transcript_url = wait_for_transcription_job('sample-job')
print(transcript_url)