
import openai
from dotenv import load_dotenv, find_dotenv


_ = load_dotenv(find_dotenv())

client = openai.Client()

def generate_text(
    messages
):

    response = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
        temperature=0,
        max_tokens=1000,
        stream=True
    )
    print()
    print("Assistant: ", end="")

    full_response = ''

    for response_stream in response:
        text = response_stream.choices[0].delta.content
        if text:
            print(text, end='')
            full_response += text

    print()

    messages.append({"role":"assistant", "content": full_response})
    return messages

def main():
    print("Welcome to a chatbot made with Python!")
    messages = []
    while True:
        print()
        user_input = input("You: ")
        messages.append({"role":"user", "content":user_input})
        messages = generate_text(messages)
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

if __name__ == "__main__":
    main()
