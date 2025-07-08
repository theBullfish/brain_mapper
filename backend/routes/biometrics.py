from fastapi import APIRouter
from pydantic import BaseModel
import sqlite3, os, pathlib

router = APIRouter()
DB = pathlib.Path(os.getenv('DB_PATH', '/mnt/data/bear_poking.sqlite'))
conn = sqlite3.connect(DB)
conn.execute('''CREATE TABLE IF NOT EXISTS hrv_window(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id TEXT,
  ts INTEGER,
  rr_ms INTEGER
)''')
conn.commit()

class HRV(BaseModel):
    user_id:str
    ts:int
    rr:int

@router.post('/biometrics')
def post_hrv(pkt:HRV):
    conn.execute("INSERT INTO hrv_window(user_id,ts,rr_ms) VALUES(?,?,?)",
                 (pkt.user_id, pkt.ts, pkt.rr))
    conn.commit()
    return {'status':'ok'}
