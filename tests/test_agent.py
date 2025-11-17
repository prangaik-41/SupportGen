# Basic test for SupportGen

from src.agent import SupportAgent

def test_basic_complaint_flow():
    agent = SupportAgent()
    out = agent.handle_complaint("u1", "I was charged twice for my order.")
    assert "reply_text" in out
    assert out["category"] == "billing"
