"""Adaptive question generator (safe)."""
import random, pathlib, yaml
from typing import Dict, Any, List

_BANK = pathlib.Path(__file__).with_name("question_bank.yaml")
_TEMPLATES: List[Dict[str, Any]] = yaml.safe_load(_BANK.read_text()) or []

class _Bandit:
    def pick(self, pool: List[Dict[str, Any]]) -> Dict[str, Any]:
        return random.choice(pool)

bandit = _Bandit()

def _age_ok(q: Dict[str, Any]) -> bool:
    ar = q.get("age_range")
    if ar is None:
        return True
    if isinstance(ar, str):
        return "adult" in ar
    try:
        return "adult" in ar
    except TypeError:
        return True

def next_question(profile: Dict[str, Any], fatigue: bool) -> Dict[str, Any]:
    pool = [q for q in _TEMPLATES if _age_ok(q)]
    if fatigue and pool:
        last_fmt = profile.get("last_format")
        pool = [q for q in pool if q["format"] != last_fmt] or pool
    return bandit.pick(pool or _TEMPLATES or [{"id": 0, "prompt": "(no templates)"}])
