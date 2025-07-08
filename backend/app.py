from fastapi import FastAPI
from .routes import biometrics, eeg

app = FastAPI()
app.include_router(biometrics.router, prefix="/api")
app.include_router(eeg.router, prefix="/api")
