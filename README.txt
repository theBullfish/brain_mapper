Patch‑A  (HRV + EEG base, control‑energy task)

1. backend/
   • app.py – FastAPI root
   • eeg_filter.py – notch + band‑pass + artefact reject
   • routes/biometrics.py – Polar HRV endpoint
   • routes/eeg.py – Muse EEG endpoint

2. frontend/apps/web/pages/control-energy.tsx – quick prototype UI

Run backend:
  uvicorn backend.app:app --reload

Run frontend:
  pnpm --filter @bear-poking/web dev

DB file defaults to /mnt/data/bear_poking.sqlite (override with DB_PATH env).
