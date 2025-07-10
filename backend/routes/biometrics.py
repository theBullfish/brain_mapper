from fastapi import APIRouter
from pydantic import BaseModel
import sqlite3

# NEW → pulls the correct path (./data/bear_poking.sqlite by default)
from ..settings import DB_PATH

router = APIRouter()

# open (or create) the SQLite database
conn = sqlite3.connect(DB_PATH)

# make sure the table exists
conn.execute(
    '''
    CREATE TABLE IF NOT EXISTS hrv_window (
        id       INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id  TEXT,
        ts       INTEGER,
        rr_ms    INTEGER,
        ack      INTEGER DEFAULT 0
    )
    '''
)
conn.commit()

# ---------- schema for incoming packets ----------
class HRVPacket(BaseModel):
    user_id: str
    ts: int          # Unix ms timestamp
    rr: int          # R–R interval in ms

# ---------- POST /api/biometrics ----------
@router.post("/biometrics")
def post_hrv(pkt: HRVPacket):
    conn.execute(
        "INSERT INTO hrv_window (user_id, ts, rr_ms) VALUES (?,?,?)",
        (pkt.user_id, pkt.ts, pkt.rr),
    )
    conn.commit()
    return {"status": "ok"}
