# Demo Instructions

1. Start the mock ticket API:
   `python src/tools/mock_ticket_api.py`

2. Run the agent demo:
   `python -m src.agent --demo`

3. Inspect logs:
   `cat logs/events.jsonl`

4. Run evaluation:
   `python -m src.eval --eval-path data/sample_complaints.json`

5. To test an interactive single request via the adapter:
   - Start the mock API
   - In Python REPL:
     ```
     from src.agent import SupportAgent
     a = SupportAgent()
     res = a.handle_complaint("u999", "My order was charged twice for ORD9999", metadata={"order_id":"ORD9999"})
     print(res)
     ```
