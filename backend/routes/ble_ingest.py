from fastapi import APIRouter
from pydantic import BaseModel
from ..ble_queue import enqueue, start_worker      # <- uses the queue writer

router = APIRouter()
start_worker()                                      # background writer thread

# ── HRV packets ─────────────────────────────────────
class HRVIn(BaseModel):
    user_id: str
    ts: int           # Unix ms
    rr: int           # R-R interval ms

@router.post("/ble/hrv")
def ingest_hrv(p: HRVIn):
    enqueue({"type": "hrv", "user_id": p.user_id, "ts": p.ts, "rr": p.rr})
    return {"status": "queued"}

# ── BEN snapshots ───────────────────────────────────
class BenIn(BaseModel):
    user_id: str
    ts_start: int     # epoch start ms
    ben: float        # brain-entropy level

@router.post("/ble/ben")
def ingest_ben(p: BenIn):
    enqueue({"type": "eeg", "user_id": p.user_id, "ts_start": p.ts_start, "ben": p.ben})
    return {"status": "queued"}
