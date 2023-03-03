import openai


def send_to_chat(messages):
    chat_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=100
    )

    # Get chat response from OpenAI Chat API
    print(f"Usage: {chat_response.usage}")
    return chat_response.choices[0].message.content
