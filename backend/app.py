from fastapi import FastAPI
from .routes import biometrics, eeg, ble_ingest

app = FastAPI()

app.include_router(biometrics.router, prefix="/api")
app.include_router(eeg.router, prefix="/api")
app.include_router(ble_ingest.router, prefix="/api")
