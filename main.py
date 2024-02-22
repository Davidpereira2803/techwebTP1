import uvicorn

if __name__ == '__main__':
    uvicorn.run("book_management.app:app", log_level = "info", port = 8000)