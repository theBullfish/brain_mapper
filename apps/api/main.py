
from fastapi import FastAPI

app = FastAPI()

@app.get("/parse")
async def parse(text: str):
    # TODO: replace with real ML
    return {"emotion": "neutral", "salience": 0.5}
