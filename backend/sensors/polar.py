"""Async Polar H10 reader – safe stub."""
import asyncio
from typing import AsyncIterable
from backend.sensors import update_sensor
from backend.pipeline.bus import publish

async def polar_stream() -> AsyncIterable[dict]:
    """Yield dummy HRV data once per second; mark sensor ok."""
    update_sensor("polar", "ok")
    while True:
        await asyncio.sleep(1)
        sample = {"ts": asyncio.get_running_loop().time(), "ibi_ms": 1000}
        await publish({"source": "hrv", **sample})
        yield sample
