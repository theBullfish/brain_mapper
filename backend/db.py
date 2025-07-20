import asyncio
"""Tiny SQLite wrapper (works anywhere)."""
import asyncio, aiosqlite, pathlib, json

_DB = pathlib.Path("ripple.sqlite").as_posix()
_POOL: aiosqlite.Connection | None = None
_LOCK = asyncio.Lock()

async def _get_conn():
    global _POOL
    async with _LOCK:
        if _POOL is None:
            _POOL = await aiosqlite.connect(_DB)
            await _POOL.execute("""
            CREATE TABLE IF NOT EXISTS ripple_bit (
              id    INTEGER PRIMARY KEY AUTOINCREMENT,
              ts    TEXT NOT NULL,
              gist  TEXT NOT NULL,
              payload TEXT NOT NULL
            )
            """)
            await _POOL.commit()
        return _POOL

async def insert_ripple(ts: str, gist: str, payload: str):
    db = await _get_conn()
    await db.execute(
        "INSERT INTO ripple_bit (ts, gist, payload) VALUES (?,?,?)",
        (ts, gist, payload),
    )
    await db.commit()

async def count_rows() -> int:
    db = await _get_conn()
    async with db.execute("SELECT COUNT(*) FROM ripple_bit") as cur:
        (n,) = await cur.fetchone()
    return n
