Patch‑C  (BLE ingest queue + /ble endpoints)

• backend/settings.py – defaults DB_PATH to ./data/bear_poking.sqlite
• backend/ble_queue.py – background worker writes HRV/EEG packets
• backend/routes/ble_ingest.py – POST /api/ble/hrv  and /api/ble/ben

Test:
  curl -X POST http://localhost:8000/api/ble/hrv -H 'Content-Type: application/json'        -d '{"user_id":"parent","ts":123456,"rr":800}'
  curl -X POST http://localhost:8000/api/ble/ben -H 'Content-Type: application/json'        -d '{"user_id":"parent","ts_start":123456,"ben":0.75}'

Both return {"status":"queued"} and rows appear in SQLite.
