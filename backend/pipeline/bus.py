"""Fan-in bus merges sensor events once per second."""
import asyncio, json
from typing import Dict, List
from backend.features import extract_features

_queue: "asyncio.Queue[Dict]" = asyncio.Queue()

async def publish(event: Dict):
    await _queue.put(event)

async def run():
    batch: List[Dict] = []
    last_emit = asyncio.get_event_loop().time()
    while True:
        try:
            evt = await asyncio.wait_for(_queue.get(), timeout=0.2)
            batch.append(evt)
        except asyncio.TimeoutError:
            pass
        now = asyncio.get_event_loop().time()
        if now - last_emit >= 1:
            if batch:
                await extract_features(batch)
                from backend.ws.manager import broadcast
                broadcast(batch[-1] if batch else {})
                batch.clear()
            last_emit = now
