from backend.memory.ripple import write as write_ripple
"""Dispatch to per-modality extractors."""
from typing import List, Dict
from backend.features import eeg as _eeg, hrv as _hrv, vision as _vis

async def extract_features(batch: List[Dict]):
    feats: Dict = {}
    feats.update(_eeg.extract([e for e in batch if e.get("source") == "eeg"]))
    feats.update(_hrv.extract([e for e in batch if e.get("source") == "hrv"]))
    feats.update(_vis.extract([e for e in batch if e.get("source") == "vision"]))
    print("FEATURE", feats)
    from backend.memory.ripple import write as write_ripple
    write_ripple(feats)
