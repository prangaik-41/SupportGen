# src/tools/mock_ticket_api.py
from flask import Flask, request, jsonify
from uuid import uuid4
import datetime

app = Flask(__name__)
TICKETS = {}

@app.route("/create_ticket", methods=["POST"])
def create_ticket():
    payload = request.get_json(force=True)
    ticket_id = "T-" + uuid4().hex[:8].upper()
    record = {
        "ticket_id": ticket_id,
        "user_id": payload.get("user_id"),
        "category": payload.get("category"),
        "summary": payload.get("summary"),
        "suggested_resolution": payload.get("suggested_resolution"),
        "metadata": payload.get("metadata", {}),
        "status": "created",
        "created_at": datetime.datetime.utcnow().isoformat() + "Z"
    }
    TICKETS[ticket_id] = record
    return jsonify(record), 201

@app.route("/ticket/<ticket_id>", methods=["GET"])
def get_ticket(ticket_id):
    ticket = TICKETS.get(ticket_id)
    if not ticket:
        return jsonify({"error": "not found"}), 404
    return jsonify(ticket), 200

if __name__ == "__main__":
    # Run: python src/tools/mock_ticket_api.py
    app.run(host="0.0.0.0", port=5001, debug=True)
