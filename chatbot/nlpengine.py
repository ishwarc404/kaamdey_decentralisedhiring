
#import library
import speech_recognition as sr
import requests
import shortuuid
import soundfile as sf



# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()


def voicetotext(url):

    # Reading Audio file
    r = requests.get(url, allow_redirects=True)
    audiofile = shortuuid.ShortUUID().random(length=5)
    open('audio/{}.ogg'.format(audiofile), 'wb').write(r.content)

    # # listening the audio file and store in audio_text variable
    data, samplerate = sf.read('audio/{}.ogg'.format(audiofile))
    sf.write('audio/{}.wav'.format(audiofile), data, samplerate)

    # with sr.AudioFile('audio/{}.wav'.format(audiofile)) as source:
    #     audio_text = r.listen(source)
        
    # # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    #     try:
    
    #         # using google speech recognition
    #         text = r.recognize_google(audio_text)
    #         text_recognised =  text 
        
    #     except:
    #         text_recognised = False





voicetotext("https://s3-external-1.amazonaws.com/media.twiliocdn.com/ACd57aa19bfb993457ee43f94e2be4c7f9/c9431049718c9b8d76ebc1c955ba72b6")






# from google.cloud import speech_v1
# from google.cloud.speech_v1 import enums
# import io


# def sample_long_running_recognize():
#     """
#     Transcribe a long audio file using asynchronous speech recognition
#     Args:
#       local_file_path Path to local audio file, e.g. /path/audio.wav
#     """

#     client = speech_v1.SpeechClient()

#     local_file_path = './test.wav'

#     # The language of the supplied audio
#     language_code = "en-US"

#     # Sample rate in Hertz of the audio data sent
#     sample_rate_hertz = 16000

#     # Encoding of audio data sent. This sample sets this explicitly.
#     # This field is optional for FLAC and WAV audio formats.
#     encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16
#     config = {
#         "language_code": language_code,
#         "sample_rate_hertz": sample_rate_hertz,
#         "encoding": encoding,
#     }
#     with io.open(local_file_path, "rb") as f:
#         content = f.read()
#     audio = {"content": content}

#     operation = client.long_running_recognize(config, audio)

#     print(u"Waiting for operation to complete...")
#     response = operation.result()

#     for result in response.results:
#         # First alternative is the most probable result
#         alternative = result.alternatives[0]
#         print(u"Transcript: {}".format(alternative.transcript))


# sample_long_running_recognize()