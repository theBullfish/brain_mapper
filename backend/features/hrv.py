from typing import List, Dict
def extract(events: List[Dict]) -> Dict:
    return {"rmssd": 0} if events else {}
