import openai
from constants import CHAT_MODEL_GPT, CHAT_MODEL_DAVINCI


def get_chat_response_gpt(messages):
    completion = openai.ChatCompletion.create(
        model=CHAT_MODEL_GPT,
        messages=messages,
        max_tokens=100
    )

    print(f"Usage: {completion.usage}")

    return completion.choices[0].message.content


def get_chat_response_davinci(messages):
    completion = openai.Completion.create(
        model=CHAT_MODEL_DAVINCI,
        prompt=messages[-1]["content"],
    )

    print(f"Usage: {completion.usage}")

    return completion.choices[0].text
