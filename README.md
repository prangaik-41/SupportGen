# SupportGen — AI Customer Support Ticket Automation Agent

## 1. Elevator pitch
Problem: Customer support teams spend significant time manually triaging, summarizing, and drafting responses to repetitive support tickets, leading to delays and inconsistent resolutions.

Solution: SupportGen automates the end‑to‑end ticket workflow using a coordinated multi‑agent system capable of classification, summarization, knowledge‑based response drafting, and final quality assurance.

Value: Reduces manual triage and drafting time by 60–80%, increases accuracy and consistency, and enables support teams to focus on complex, high‑value customer issues.

## 2. Core concept & novelty
- Why agents?
- Support tickets require interpretation, reasoning, and tool usage—tasks that static ML systems struggle with. Agents allow SupportGen to adapt, reason through escalating complexity, and interact with internal tools such as ticket APIs and knowledge bases.
- 
- Key Concepts Demonstrated:
Multi‑Agent Pipeline: Classifier → Summarizer → Response Generator → QA Validator → Publisher.
Tool Use: Mock ticket API, knowledge base search, and structured output validation.
Sessions & State: Ticket‑level state tracking with contextual memory.
Long‑Term Memory: Stores historical customer patterns and recurring issue signatures.
Observability: Structured logs and traces for debugging cross‑agent workflows.

## 3. Architecture
- Short description
- `docs/architecture.png` (diagram)

## 4. How to run (reproducible)
Prereqs: Python 3.10, pip
Commands:
- `pip install -r requirements.txt`
- `python src/tools/mock_ticket_api.py`
- `python src/agent.py --demo`
- `python src/eval.py --eval-set data/eval_set.csv`

## 5. Files & structure
List main files and explanation.

## 6. Evaluation
- Datasets used
- Metrics (Table + short discussion)
- `reports/eval_report.json` (link)

## 7. Deployment
- Dockerfile + steps (or Cloud Run instructions)

## 8. Video
YouTube link: <paste link>

## 9. Limitations & future work
Short bullets.

## 10. Team
Names and roles.

## 11. License & credits
