import os, pathlib
DEFAULT_DIR = pathlib.Path(__file__).resolve().parent.parent.parent / "data"
DEFAULT_DIR.mkdir(exist_ok=True)
DB_PATH = pathlib.Path(os.getenv("DB_PATH", DEFAULT_DIR / "bear_poking.sqlite"))
