from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from users.router import router as user_router
from users import models as user_models
from database import engine

user_models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="My app", version="0.1.0")

origins = [
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(user_router, tags=["Users"], prefix="/api/users")


@app.get("/api/healthcheck")
def root():
    return {"message": "Hello world"}
