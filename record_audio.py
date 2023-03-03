import speech_recognition as sr
from constants import AUDIO_FILE_NAME


def record_audio():
    r = sr.Recognizer()
    print("Listening...")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=2) # Stop listening after 2 seconds of silence
    print("Processing...")

    with open(AUDIO_FILE_NAME, "wb") as f:
        f.write(audio.get_wav_data())
