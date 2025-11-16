# src/agent.py
import argparse
import time
from src.llm_client import MockLLMClient
from src.tools.ticket_adapter import TicketAdapter
from src.memory import JSONMemory
from src.logger import JSONLogger

# NOTE: relative imports assume you run from project root. If running directly, adjust PYTHONPATH.

class SupportAgent:
    def __init__(self, llm_client=None, ticket_adapter=None, memory=None, logger=None):
        self.llm = llm_client or MockLLMClient()
        self.ticket_adapter = ticket_adapter or TicketAdapter()
        self.memory = memory or JSONMemory()
        self.logger = logger or JSONLogger()

    def _plan_action(self, category: str, classification_conf: float) -> dict:
        """
        Decide whether to create a ticket. Simple rule:
         - For billing, technical, delivery, refund => create ticket
         - For account => suggest reset (no ticket) but can create if severe
        """
        create_ticket = category in {"billing", "technical", "delivery", "refund"}
        action = "create_ticket" if create_ticket else "suggest_resolution"
        return {"action": action, "reason": f"default_rule_for_{category}"}

    def handle_complaint(self, user_id: str, text: str, metadata: dict=None) -> dict:
        start_ts = time.time()

        cat, conf = self.llm.classify(text)
        recent = self.memory.get_recent(user_id, n=2)
        memory_context = "\n".join([r.get("complaint","") for r in recent]) if recent else None

        reply = self.llm.generate_reply(cat, text, memory_context=memory_context)
        plan = self._plan_action(cat, conf)

        ticket = None
        if plan["action"] == "create_ticket":
            # create ticket via adapter
            ticket = self.ticket_adapter.create_ticket(user_id=user_id,
                                                       category=cat,
                                                       summary=text[:200],
                                                       suggested_resolution=reply,
                                                       metadata=metadata or {})
            ticket_id = ticket.get("ticket_id") if ticket else None
        else:
            ticket_id = None

        # Save memory
        self.memory.append_interaction(user_id=user_id, complaint=text, ticket_id=ticket_id, resolution=reply)

        # Logging
        self.logger.log({
            "event": "handled_complaint",
            "user_id": user_id,
            "category": cat,
            "confidence": conf,
            "action": plan["action"],
            "ticket_id": ticket_id,
            "latency_ms": int((time.time() - start_ts) * 1000)
        })

        out = {
            "user_id": user_id,
            "category": cat,
            "confidence": conf,
            "reply_text": reply,
            "ticket": ticket,
            "action": plan["action"]
        }
        return out

def demo_run():
    agent = SupportAgent()
    samples = [
        ("u001", "I was charged twice for order ORD1001. Please refund."),
        ("u002", "My internet disconnects every 10 minutes."),
        ("u003", "Where is my package? It's late."),
        ("u004", "I forgot my password and can't login.")
    ]
    for uid, text in samples:
        print(f"---\nUser {uid} says: {text}")
        res = agent.handle_complaint(user_id=uid, text=text)
        print("Response:", res["reply_text"])
        print("Ticket:", res["ticket"]["ticket_id"] if res.get("ticket") else None)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true", help="Run demo examples")
    args = parser.parse_args()
    if args.demo:
        demo_run()
    else:
        print("Run with --demo to see sample flow.")
