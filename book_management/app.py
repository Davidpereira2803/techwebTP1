from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from book_management.routes.routes import router
from book_management.routes.users_routes import login_router
from book_management.database import create_database

templates = Jinja2Templates(directory="templates")

app = FastAPI(title = "My Library")
app.mount("/static", StaticFiles(directory="static"))
app.include_router(router)
app.include_router(login_router)

@app.on_event('startup')
def on_startup():
    print("Library Server has started!")
    create_database()

@app.on_event('shutdown')
def on_shutdown():
    print("Library Server is down!")

@app.exception_handler(404)
def custom_404_redirection(request: Request, exception: HTTPException):
    return templates.TemplateResponse("errors/404.html", {"request": request, "exception": exception}, status_code=404)

@app.exception_handler(400)
def custom_400_redirection(request: Request, exception: HTTPException):
    return templates.TemplateResponse("errors/400.html", {"request": request, "exception": exception}, status_code=400)

@app.exception_handler(422)
def custom_422_redirection(request: Request, exception: HTTPException):
    return templates.TemplateResponse("errors/422.html", {"request": request, "exception": exception}, status_code=422)

@app.exception_handler(401)
def custom_422_redirection(request: Request, exception: HTTPException):
    return templates.TemplateResponse("errors/401.html", {"request": request, "exception": exception}, status_code=401)
