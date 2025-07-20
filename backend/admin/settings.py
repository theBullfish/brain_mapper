_settings = {"focus_threshold_pct": 15, "focus_window_sec": 7}

def get(key):  return _settings[key]
def set(key, val): _settings[key] = val
