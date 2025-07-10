"""
Thread-safe queue that writes packets to SQLite.
Stub version; replace with Redis later.
"""
import queue, threading, sqlite3, time
from .settings import DB_PATH

_q     = queue.Queue()
_stop  = threading.Event()

def enqueue(pkt: dict):
    _q.put(pkt)

def _worker():
    conn = sqlite3.connect(DB_PATH)
    while not _stop.is_set():
        try:
            pkt = _q.get(timeout=1)
        except queue.Empty:
            continue

        if pkt["type"] == "hrv":
            conn.execute(
                "INSERT INTO hrv_window (user_id, ts, rr_ms) VALUES (?,?,?)",
                (pkt["user_id"], pkt["ts"], pkt["rr"]),
            )
        elif pkt["type"] == "eeg":
            conn.execute(
                "INSERT INTO eeg_epoch (user_id, ts_start, ben_level) VALUES (?,?,?)",
                (pkt["user_id"], pkt["ts_start"], pkt["ben"]),
            )
        conn.commit()
        _q.task_done()

def start_worker():
    threading.Thread(target=_worker, daemon=True).start()
