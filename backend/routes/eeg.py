from fastapi import APIRouter
from pydantic import BaseModel
import numpy as np, sqlite3, os, pathlib
from ..eeg_filter import notch_filter, band_pass, artefact_mask

router = APIRouter()
DB = pathlib.Path(os.getenv('DB_PATH', '/mnt/data/bear_poking.sqlite'))
conn = sqlite3.connect(DB)
conn.execute('''CREATE TABLE IF NOT EXISTS eeg_epoch(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id TEXT,
  ts_start INTEGER,
  ben_level REAL
)''')
conn.commit()

class Epoch(BaseModel):
    user_id:str
    ts_start:int
    fs:int
    data:list

@router.post('/eeg')
def post_eeg(ep:Epoch):
    arr = np.array(ep.data).reshape((4,-1))
    arr = band_pass(notch_filter(arr, ep.fs), ep.fs)
    mask = artefact_mask(arr)
    ben = float(np.mean(np.var(arr[:,mask], axis=-1))) if mask.any() else 0.0
    conn.execute("INSERT INTO eeg_epoch(user_id,ts_start,ben_level) VALUES(?,?,?)",
                 (ep.user_id, ep.ts_start, ben))
    conn.commit()
    return {'status':'ok'}
