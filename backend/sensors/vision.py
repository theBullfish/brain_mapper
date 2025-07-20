"""Selfie-cam vision stub."""
import asyncio
from typing import AsyncIterable
from backend.sensors import update_sensor
from backend.pipeline.bus import publish

async def vision_stream() -> AsyncIterable[dict]:
    """Yield dummy gaze + expression each second; mark sensor ok."""
    update_sensor("vision", "ok")
    while True:
        await asyncio.sleep(1)
        sample = {
            "ts": asyncio.get_running_loop().time(),
            "gaze": [0.0, 0.0],
            "expr": "neutral",
        }
        await publish({"source": "vision", **sample})
        yield sample
