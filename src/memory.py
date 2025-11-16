# src/memory.py
import json
import os
from datetime import datetime
from typing import List, Dict

class JSONMemory:
    def __init__(self, path="data/memory.json"):
        self.path = path
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump({}, f)

    def _read(self) -> Dict[str, List[Dict]]:
        with open(self.path, "r") as f:
            return json.load(f)

    def _write(self, data: Dict[str, List[Dict]]):
        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)

    def append_interaction(self, user_id: str, complaint: str, ticket_id: str=None, resolution: str=None):
        data = self._read()
        entries = data.get(user_id, [])
        entries.append({
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "complaint": complaint,
            "ticket_id": ticket_id,
            "resolution": resolution
        })
        data[user_id] = entries[-20:]  # keep last 20
        self._write(data)

    def get_recent(self, user_id: str, n=2) -> List[Dict]:
        data = self._read()
        return data.get(user_id, [])[-n:]
