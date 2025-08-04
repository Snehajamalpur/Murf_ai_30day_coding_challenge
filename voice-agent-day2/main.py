from fastapi import FastAPI, Request
from pydantic import BaseModel
import requests
import os
import uuid
from dotenv import load_dotenv
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Serve static files from 'audio_files' directory
app.mount("/audio", StaticFiles(directory="audio_files"), name="audio")

# Get API key from environment
MURF_API_KEY = os.getenv("MURF_API_KEY")

# Ensure audio directory exists
os.makedirs("audio_files", exist_ok=True)

# TTS input model
class TTSRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "TTS API is running!"}

@app.get("/tts/")
def tts_get(text: str):
    try:
        # Prepare request
        url = "https://api.murf.ai/v1/tts/generate"
        headers = {
            "Authorization": f"Bearer {MURF_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "text": text,
            "voice": "en-US-wavenet-D"  # Modify voice as needed
        }

        # Call Murf TTS API
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        audio_data = response.content

        # Save audio file
        file_name = f"{uuid.uuid4()}.mp3"
        file_path = os.path.join("audio_files", file_name)
        with open(file_path, "wb") as f:
            f.write(audio_data)

        # Return audio URL
        return {"audio_url": f"http://127.0.0.1:8000/audio/{file_name}"}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/ui")
def serve_ui():
    return FileResponse("main.html")
