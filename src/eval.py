# src/eval.py
import json
import argparse
from src.agent import SupportAgent
from difflib import SequenceMatcher
import time
import os

def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a or "", b or "").ratio()

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def evaluate(eval_path="data/sample_complaints.json"):
    data = load_json(eval_path)
    agent = SupportAgent()
    results = []
    for item in data:
        uid = item.get("user_id", "uX")
        text = item["text"]
        expected_cat = item.get("expected_category")
        expected_action = item.get("expected_action")
        expected_reply = item.get("expected_reply", "")

        t0 = time.time()
        out = agent.handle_complaint(user_id=uid, text=text)
        latency = (time.time() - t0) * 1000

        got_cat = out["category"]
        got_action = out["action"]
        got_reply = out["reply_text"]
        sim = similarity(got_reply, expected_reply)
        ticket_created = bool(out.get("ticket"))

        results.append({
            "user_id": uid,
            "text": text,
            "expected_cat": expected_cat,
            "got_cat": got_cat,
            "expected_action": expected_action,
            "got_action": got_action,
            "ticket_created": ticket_created,
            "reply_similarity": sim,
            "latency_ms": latency
        })

    # compute metrics
    total = len(results)
    cat_acc = sum(1 for r in results if r["expected_cat"] == r["got_cat"]) / total
    action_acc = sum(1 for r in results if r["expected_action"] == r["got_action"]) / total
    avg_sim = sum(r["reply_similarity"] for r in results) / total
    avg_latency = sum(r["latency_ms"] for r in results) / total

    report = {
        "total": total,
        "category_accuracy": round(cat_acc, 4),
        "action_accuracy": round(action_acc, 4),
        "avg_reply_similarity": round(avg_sim, 4),
        "avg_latency_ms": round(avg_latency, 2)
    }
    # Save report
    os.makedirs("reports", exist_ok=True)
    with open("reports/eval_report.json", "w") as f:
        json.dump({"report": report, "results": results}, f, indent=2)
    print("Evaluation report saved to reports/eval_report.json")
    print(report)
    return report

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--eval-path", default="data/sample_complaints.json")
    args = parser.parse_args()
    evaluate(args.eval_path)
