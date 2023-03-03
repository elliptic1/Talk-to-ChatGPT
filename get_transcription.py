import openai
import os
from constants import AUDIO_FILE_NAME, SPEECH_TO_TEXT_MODEL


def get_transcription():
    # Load audio file and send to Whisper for transcription
    with open(AUDIO_FILE_NAME, "rb") as audio_file:
        transcript = openai.Audio.transcribe(SPEECH_TO_TEXT_MODEL, audio_file)

    os.remove(AUDIO_FILE_NAME)

    return transcript
