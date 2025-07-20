"""Async Muse 2 reader – safe stub (no BLE needed)."""
import asyncio
from typing import AsyncIterable
from backend.sensors import update_sensor
from backend.pipeline.bus import publish

MUSE_SERVICE_UUID = "0000fe8d-0000-1000-8000-00805f9b34fb"

async def muse_stream() -> AsyncIterable[dict]:
    """Yield dummy EEG every second; mark sensor ok."""
    update_sensor("muse", "ok")
    while True:
        await asyncio.sleep(1)
        sample = {"ts": asyncio.get_running_loop().time(), "ch": [0, 0, 0, 0]}
        await publish({"source": "eeg", **sample})
        yield sample
