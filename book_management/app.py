from fastapi import FastAPI

from book_management.routes.routes import router

app = FastAPI(title = "My Library")
app.include_router(router)

@app.on_event('startup')
def on_startup():
    print("Library Server has started!")

@app.on_event('shutdown')
def on_shutdown():
    print("Library Server is down!")