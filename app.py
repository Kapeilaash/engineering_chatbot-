from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape

BASE_DIR = Path(__file__).parent
TEMPLATE_DIR = BASE_DIR / 'src' / 'templates'
STATIC_DIR = BASE_DIR / 'src' / 'static'

app = FastAPI(title='Engineering Chatbot')
app.mount('/static', StaticFiles(directory=str(STATIC_DIR)), name='static')

env = Environment(
    loader=FileSystemLoader(str(TEMPLATE_DIR)),
    autoescape=select_autoescape(['html', 'xml'])
)

@app.get('/', response_class=HTMLResponse)
async def root():
    template = env.get_template('chat.html')
    return template.render()

@app.post('/api/chat')
async def chat(payload: dict):
    user_message = payload.get('message', '')
    # Placeholder logic for chatbot response
    reply = f"You said: {user_message}" if user_message else "Please say something."
    return JSONResponse({'reply': reply})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('app:app', host='0.0.0.0', port=8000, reload=True)
