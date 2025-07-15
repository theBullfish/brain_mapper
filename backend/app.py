from fastapi import FastAPI
from backend.routes import biometrics

app = FastAPI()
app.include_router(biometrics.router)
