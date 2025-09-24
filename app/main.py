from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/move", response_class=HTMLResponse)
async def make_move(request: Request):
    form_data = await request.form()
    move = form_data.get("move")
    # Here you would add logic to process the move and update the game state
    return templates.TemplateResponse("index.html", {"request": request, "message": f"Move {move} received!"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)