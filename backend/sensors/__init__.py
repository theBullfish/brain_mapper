"""Sensor status registry shared across the backend."""
from __future__ import annotations
from typing import Dict

_registry: Dict[str, str] = {"muse": "unknown", "polar": "unknown", "vision": "unknown"}

def update_sensor(name: str, status: str) -> None:
    _registry[name] = status

def get_registry() -> Dict[str, str]:
    return dict(_registry)
