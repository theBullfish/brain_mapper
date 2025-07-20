"""Persist a tiny “ripple” gist for each feature burst."""
import asyncio, hashlib, json, datetime
from typing import Dict
from backend.db import insert_ripple

_MEM: list[Dict] = []          # in-memory cache for quick /mem/latest

async def _persist(ts: str, gist: str, payload: str):
    """Fire-and-forget DB insert."""
    try:
        await insert_ripple(ts, gist, payload)
    except Exception:  # noqa: BLE001 – keep bursts flowing even if DB down
        pass

def write(feature: Dict):
    """Compute gist, store in memory, enqueue async DB insert."""
    payload = json.dumps(feature, sort_keys=True)
    gist = hashlib.sha256(payload.encode()).hexdigest()[:64]
    ts = datetime.datetime.utcnow().isoformat()

    _MEM.append({"ts": ts, "gist": gist, "payload": feature})
    if len(_MEM) > 300:          # cap memory buffer
        _MEM.pop(0)

    asyncio.create_task(_persist(ts, gist, payload))

def latest(n: int = 20):
    """Return last *n* ripple rows (default 20)."""
    return _MEM[-n:]
