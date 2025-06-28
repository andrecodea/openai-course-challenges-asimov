import openai
import playsound3
import speech_recognition as sr
import pyaudio
from pathlib import Path
import sounddevice
from io import BytesIO
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
client = openai.Client()

AUDIO_FILE = 'assistant_speech.mp3'

recognizer = sr.Recognizer()

# Records audio from the user's microphone
def record_audio():
    with sr.Microphone() as source:
        print('Listening...')
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    return audio

# Transcribes the recorded audio using OpenAI Whisper API
def transcribe_audio(audio):
    wav_data = BytesIO(audio.get_wav_data())
    wav_data.name = 'audio.wav'
    transcription = client.audio.transcriptions.create(
        model='whisper-1',
        file=wav_data
    )
    return transcription.text

# Gets a response from the OpenAI Chat API based on the conversation history
def complete_text(messages):
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=messages,
        max_tokens=1000,
        temperature=0
    )
    return response

# Converts the assistant's text response to speech and saves it as an audio file
def create_audio(text):
    if Path(AUDIO_FILE).exists():
        Path(AUDIO_FILE).unlink()
    response = client.audio.speech.create(
        model='tts-1',
        voice='onyx',
        input=text
    )
    response.write_to_file(AUDIO_FILE)

# Plays the generated audio file
def play_audio():
    playsound3.playsound(AUDIO_FILE)

# Main loop: records, transcribes, gets response, generates and plays audio
def main():
    messages = []
    while True:
        audio = record_audio()
        transcription = transcribe_audio(audio)
        messages.append({'role':'user', 'content':transcription})
        print(f"User: {messages[-1]['content']}")
        response = complete_text(messages)
        messages.append({'role':'assistant', 'content':response.choices[0].message.content})
        print(f"Assistant: {messages[-1]['content']}")
        create_audio(messages[-1]['content'])
        play_audio()


if __name__ == "__main__":
    main()