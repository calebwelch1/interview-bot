# send audio and transcribe
# send transcription to chatgpt and get resposne
# save chat history to send back and forth for context

from fastapi import FastAPI, UploadFile
from fastapi.responses import StreamingResponse
from dotenv import load_dotenv

import json
import os
import requests
import openai
from openai import OpenAI
load_dotenv()

openai_apikey = os.getenv("OPEN_AI_KEY")
openai_orgkey = os.getenv("OPEN_AI_ORG")
elevenlabs_key = os.getenv("ELEVENLABS_KEY")

app = FastAPI()

# to run server
# uvicorn main:app --reload
client = OpenAI(
  organization=openai_orgkey,
  api_key=openai_apikey,
)
# platform.openai.com/docs/libraries

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/talk")
async def post_audio(file: UploadFile):
    user_message = transcribe_audio(file)
    chat_response = get_chat_response(user_message)
    audio_output = text_to_speech(chat_response)

    def iterfile():  # 
        # with open(some_file_path, mode="rb") as file_like:  # 
        #     yield from file_like  # 
        yield audio_output

    return StreamingResponse(iterfile(), media_type="audio/mpeg")
   

# post to localhost:8000/talk with audio file in body to test

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

# function definitions

# transcribe the input audio into text for chatgpt
def transcribe_audio(file):
    audio_file= open(file.filename, "rb")
    transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file,
    # if you don't add this response is unsubscriptable
    response_format="text"
    )
    # hard code testing
    # transcript = {"role": "user", "content": "Who won world series in 2020?"}
    # print(transcript)
    # return {"message": "Audio Transcribed!"}
    # print("transcript is:", transcript, "stop")
    return transcript

def get_chat_response(user_message):
    messages = load_messages()
    # print("user message is:", user_message)
    # print("messages is:", messages, "stop")
    messages.append({"role": "user", "content": user_message})
    # send to chatgpt/openai
    # hard code for test
    # gpt_response = {"role": "assistant", "content":"The LA Dodgers"}
    # # save messages
    gpt_response = client.chat.completions.create(model="gpt-3.5-turbo",messages=messages,)

    parsed_gpt_response = gpt_response.choices[0].message.content
    # response looks like this, won't allow accessing index with ["choices"] need . notation
    # choices=[Choice(finish_reason='stop', index=0, message=ChatCompletionMessage(content="Hey there!")"
    # print(parsed_gpt_response)
    # print(user_message, "stop")
    save_messages(user_message, parsed_gpt_response)
    return parsed_gpt_response

def load_messages():
    messages = []
    file = 'database.json'

    # if file is empty we need to add the context
    # below is isempty code
    empty = os.stat(file).st_size == 0

    # if file is not empty, loop through history and add messages

    if not empty:
        with open(file) as db_file:
            data = json.load(db_file)
            for item in data:
                messages.append(item)
    else:
        messages.append(
            {"role": "system", "content": "Your are an interviewer who is interviewing the user for a front-end React developer position. Ask short questions that are relevant to a junior level developer. Your name is Matilda. Keep your responses under 30 words and be funny sometimes."}
        )
    return messages

# save messages in file
def save_messages(user_message, gpt_response):
    file = 'database.json'
    messages = load_messages()
    messages.append({"role": "user", "content": user_message}) 
    messages.append({"role": "assistant", "content": gpt_response})
    with open(file, 'w') as f:
        json.dump(messages, f)

# text to speech for the chatbot

def text_to_speech(text):
    # https://api.elevenlabs.io/docs
    body = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0,
            "similarity_boost": 0,
            "style": 0,
            "use_speaker_boost": True
        }
    }

    headers = {
        "Content-Type": "application/json",
        "accept": "audio/mpeg",
        "xi-api-key": elevenlabs_key
    }

    url = f"https://api.elevenlabs.io/v1/text-to-speech/XrExE9yKIg1WjnnlVkGX"

    try:
        response = requests.post(url, json=body, headers=headers)
        if response.status_code == 200:
            return response.content
        else:
            print('something went wrong!')
    except Exception as e:
        print(e)