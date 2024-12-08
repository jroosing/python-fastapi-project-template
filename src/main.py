from fastapi import FastAPI

app = FastAPI(title="My app", version="0.1.0")


@app.get("/")
def root():
    return {"message": "Hello world"}
