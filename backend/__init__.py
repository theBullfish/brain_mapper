import asyncio
"""Launch sensor coroutines when FastAPI boots."""
import asyncio
from backend.sensors.muse import muse_stream
from backend.sensors.polar import polar_stream
from backend.sensors.vision import vision_stream
from backend.pipeline.bus import run as bus_run  # stub vision

def start_background_tasks(app):
    """Kick off all sensor streams on startup."""
    loop = asyncio.get_event_loop()
    loop.create_task(_spawn(muse_stream()))
    loop.create_task(_spawn(polar_stream()))
    loop.create_task(_spawn(vision_stream()))
    loop.create_task(bus_run())

async def _spawn(aiter):
    async for _ in aiter:
        pass  # discard dummy data for now
