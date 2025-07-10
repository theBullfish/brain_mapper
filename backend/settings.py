import os, pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)        # create ./data if missing

DB_PATH = pathlib.Path(
    os.getenv("DB_PATH", DATA_DIR / "bear_poking.sqlite")
)
