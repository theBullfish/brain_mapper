from typing import List, Dict
def extract(events: List[Dict]) -> Dict:
    return {"gaze_x": 0, "gaze_y": 0} if events else {}
