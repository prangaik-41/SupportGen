# src/logger.py
import json
import os
from datetime import datetime

class JSONLogger:
    def __init__(self, path="logs/events.jsonl"):
        self.path = path
        os.makedirs(os.path.dirname(self.path), exist_ok=True)

    def log(self, event: dict):
        e = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            **event
        }
        with open(self.path, "a") as f:
            f.write(json.dumps(e) + "\n")
