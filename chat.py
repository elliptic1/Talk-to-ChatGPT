import os
import openai
import subprocess
import re
from record_audio import record_audio
from get_transcription import get_transcription
from get_chat_response import get_chat_response_gpt, get_chat_response_davinci


def main():
    # Set up OpenAI API credentials
    openai.api_key = os.environ["OPENAI_API_KEY"]

    messages = []

    while True:

        record_audio()

        transcript = get_transcription()

        print(f"User: {transcript.text}")

        if re.search('^[^a-zA-Z]*$', transcript.text):
            continue

        # Save user input to history
        messages.append({"role": "user", "content": f"Answer in one sentence. {transcript.text}"})

        # Get chat response from OpenAI Chat API
        chat_response = get_chat_response_gpt(messages)

        # Save response to history
        messages.append({"role": "assistant", "content": chat_response})

        # Debug print chat response
        print(f"Response: {chat_response}")

        # Speak chat response
        subprocess.run(["say", chat_response])

        # Save only the last x interactions
        messages = messages[-4:]


if __name__ == "__main__":
    main()
