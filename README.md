# OpenAI API Course

This repository contains examples and mini-projects using the OpenAI API.

## 1. Voice Recognition Chatbot CLI
Implementation of a voice chatbot that uses the OpenAI API to generate responses from audio prompts (tts-1, whisper-1, and gpt-3.5-turbo). It is capable of: capturing audio from the user via microphone, transcribing the audio to text via Whisper, generating responses with GPT-3.5-turbo, converting the response to audio via TTS, and playing the audio response back to the user.

## 2. CLI Chatbot
Implementation of a Python chatbot using the OpenAI GPT API (gpt-3.5-turbo) to generate real-time responses. I implemented a simple CLI chatbot that can receive prompts and generate text.

## 3. Finance CLI Chatbot
Implementation of a finance chatbot in Python using the OpenAI GPT API (gpt-3.5-turbo), the Yahoo Finance API, and function calling to generate real-time responses. I implemented a CLI chatbot that can receive prompts and answer them using function calling for questions about the financial market.

## Local Usage
1. Clone the repository.
2. Make sure to install the requirements from the `requirements.txt` file.
3. Add your OpenAI API key in a `.env` file.
4. Run your `chatbot.py` file.

## Requirements
The requirements can be found in the `requirements.txt` file. They can be installed via `pip`.

```bash
pip install -r requirements.txt
```