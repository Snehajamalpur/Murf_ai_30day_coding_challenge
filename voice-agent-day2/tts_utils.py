import requests
import os
from dotenv import load_dotenv

load_dotenv()

def generate_tts_audio(text: str) -> str:
    api_key = os.getenv("MURF_API_KEY")
    if not api_key:
        raise ValueError("API key not found")

    url = "https://api.murf.ai/v1/speech/generate"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "api-key": api_key
    }
    data = {
        "text": text,
        "voice": "en-US-1",
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get("audio_url", "No audio URL returned")
    else:
        raise ValueError(f"Error: {response.status_code} - {response.text}")
