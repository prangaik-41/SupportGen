# src/tools/ticket_adapter.py
import requests
import time
from typing import Optional

class TicketAdapter:
    def __init__(self, base_url="http://127.0.0.1:5001", timeout=5, max_retries=3):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries

    def create_ticket(self, user_id: str, category: str, summary: str, suggested_resolution: str, metadata: dict=None) -> Optional[dict]:
        url = f"{self.base_url}/create_ticket"
        payload = {
            "user_id": user_id,
            "category": category,
            "summary": summary,
            "suggested_resolution": suggested_resolution,
            "metadata": metadata or {}
        }
        attempt = 0
        while attempt < self.max_retries:
            try:
                resp = requests.post(url, json=payload, timeout=self.timeout)
                resp.raise_for_status()
                return resp.json()
            except requests.RequestException as e:
                attempt += 1
                time.sleep(0.5 * attempt)  # exponential-ish backoff
        return None
