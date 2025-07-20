"""Main FastAPI application with robust health checks."""

import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import pathlib

from backend.health import check_db, check_sensors
from backend.questions.generator import next_question
from backend.admin.settings import get as get_setting, set as set_setting
from backend.ws.manager import register, unregister
from backend import start_background_tasks
from backend.memory.ripple import latest as mem_latest
from backend.db import count_rows

app = FastAPI()

# Always serve static files from backend/static, regardless of cwd
STATIC_ABS = str((pathlib.Path(__file__).parent / "static").resolve())
app.mount('/static', StaticFiles(directory=STATIC_ABS), name='static')

@app.get("/admin")
async def admin_redirect():
    """Redirect to the admin.html frontend page."""
    return RedirectResponse(url="/static/admin.html")

@app.websocket("/ws/features")
async def ws_features(ws: WebSocket):
    await ws.accept()
    q = await register()
    try:
        while True:
            data = await q.get()
            await ws.send_text(data)
    except (WebSocketDisconnect, asyncio.CancelledError):
        unregister(q)

@app.get("/ping", tags=["health"])
async def ping():
    return {"status": "ok"}

@app.get("/health", tags=["health"])
async def health():
    db_status = check_db()
    sensors = check_sensors()
    status = "ok" if db_status == "ok" and all(v == "ok" for v in sensors.values()) else "degraded"
    return {"status": status, "db": db_status, **{f"sensor_{k}": v for k, v in sensors.items()}}

@app.on_event("startup")
async def _startup():
    start_background_tasks(app)

@app.post("/questions/next")
async def api_next_question(profile: dict):
    fatigue = False  # TODO: wire focus metric
    return next_question(profile, fatigue)

@app.get("/admin/settings")
async def read_settings():
    return {
        "focus_threshold_pct": get_setting("focus_threshold_pct"),
        "focus_window_sec": get_setting("focus_window_sec")
    }

@app.put("/admin/settings/{key}")
async def write_setting(key: str, val: int):
    set_setting(key, val)
    return {"ok": True}

@app.get("/mem/count", tags=["memory"])
async def mem_count():
    try:
        n = await count_rows()
        return {"rows": n}
    except Exception as err:
        return {"rows": None, "status": "db_unavailable", "detail": str(err)}

@app.get("/mem/latest", tags=["memory"])
async def mem_latest_route(n: int = 20):
    """Return last N ripple gists."""
    return mem_latest(n)

@app.get("/api/test")
async def test_route():
    return {"message": "It works!"}
