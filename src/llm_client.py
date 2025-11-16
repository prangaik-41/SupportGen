# src/llm_client.py
"""
LLM client wrapper.
Currently contains a mock deterministic implementation for offline testing.
Replace or extend this with a Gemini/OpenAI client to call real models.

To swap to a real model:
- Implement `generate_reply` and `classify` methods to call your model endpoint.
- Do not include API keys in the repo. Use env vars or secrets during deployment.
"""

from typing import Dict, Tuple
import random

class MockLLMClient:
    def __init__(self):
        # deterministic mapping to simulate classification
        self.category_keywords = {
            "billing": ["charge", "charged", "invoice", "billing", "refund", "refunds", "double charged"],
            "technical": ["disconnect", "error", "crash", "not working", "bug", "disconnects", "slow"],
            "delivery": ["where is my", "late", "delayed", "package", "shipment", "tracking"],
            "account": ["password", "login", "account", "sign in", "can't login", "forgot"],
            "refund": ["cancel", "cancel my order", "refund", "return"]
        }

    def classify(self, text: str) -> Tuple[str, float]:
        t = text.lower()
        for cat, kwlist in self.category_keywords.items():
            for kw in kwlist:
                if kw in t:
                    return cat, 0.95
        # fallback
        return "other", 0.6

    def generate_reply(self, category: str, text: str, memory_context: str=None) -> str:
        # Simple templated replies for demonstration
        if category == "billing":
            return "We're sorry to hear about the billing issue. We will review your invoice and start a refund if needed."
        if category == "technical":
            return "Apologies — we will escalate this to our technical team to investigate your connectivity issue."
        if category == "delivery":
            return "We’ll check your shipment status and update you as soon as possible."
        if category == "account":
            return "We can help reset your password. Please follow the secure reset steps we've sent to your email."
        if category == "refund":
            return "We can start the cancellation and refund process; we'll update you with the ticket status shortly."
        return "Thanks for reaching out — we will review and get back to you soon."

# Placeholder class: how to wire Gemini (commented)
class GeminiClient:
    def __init__(self, *args, **kwargs):
        # Example: store credentials from env and init client
        # self.api_key = os.getenv("GEMINI_KEY")
        # self.client = initialize_gemini_client(self.api_key)
        raise NotImplementedError("Gemini client not implemented in starter code. See README to enable.")
