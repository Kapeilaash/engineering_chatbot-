# Engineering Chatbot

Minimal FastAPI-based web UI skeleton for an engineering Q&A chatbot.

## Features
- FastAPI backend with `/api/chat` endpoint
- Simple HTML/CSS frontend (no build step)
- Live reload when run with `uvicorn --reload`

## Install
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run
```powershell
uvicorn app:app --reload
```
Open http://127.0.0.1:8000

## Customize Bot Logic
Edit `app.py` inside `chat` endpoint. Replace placeholder echo logic with your model integration.

## Project Structure
```
engineering_chatbot/
  app.py
  requirements.txt
  src/
    templates/
      chat.html
    static/
      style.css
```
