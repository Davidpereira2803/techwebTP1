from fastapi import FastAPI

from book_management.routes.routes import router

app = FastAPI(title = "My Book Shelf")
app.include_router(router)

@app.on_event('startup')
def on_startup():
    print("Book Shelf Server has started!")

@app.on_event('shutdown')
def on_shutdown():
    print("Book Shelf Server is down!")