"""Simple pub-sub so any code can broadcast JSON payloads."""
import asyncio, json
from typing import Set

_subs: Set[asyncio.Queue] = set()

async def register() -> asyncio.Queue:
    """Return a queue for one WebSocket client."""
    q: asyncio.Queue = asyncio.Queue(maxsize=100)
    _subs.add(q)
    return q

def unregister(q: asyncio.Queue):
    _subs.discard(q)

def broadcast(obj):
    """Fan-out one Python dict to all subscribers (fire-and-forget)."""
    msg = json.dumps(obj)
    for q in list(_subs):
        try:
            q.put_nowait(msg)
        except asyncio.QueueFull:   # client too slow → drop message
            _subs.discard(q)
