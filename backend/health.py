from typing import Dict
from backend.sensors import get_registry

def check_db() -> str:
    try:
        import asyncpg  # noqa: WPS433
        return "ok"
    except Exception:
        return "error"

def check_sensors() -> Dict[str, str]:
    return get_registry()
