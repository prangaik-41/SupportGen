# SupportGen — AI Customer Support Ticket Automation Agent

## 1. Elevator Pitch
**Problem:** Customer support teams spend significant time manually triaging, summarizing, and drafting responses to repetitive support tickets, leading to slower response times and inconsistent resolutions.

**Solution:** SupportGen automates the end-to-end support ticket workflow through a coordinated multi-agent system capable of classification, summarization, knowledge-based response drafting, and final quality assurance.

**Value:** Reduces manual triage and drafting time by **60–80%**, improves accuracy and consistency, and allows human support teams to focus on complex, high-impact issues.

---

## 2. Core Concept & Novelty

### Why Agents?
Static ML systems fail at tasks requiring reasoning, multi-step workflows, or tool usage. Agents solve this by enabling:

- Reasoning through ambiguous or incomplete tickets  
- Decomposing tasks into multiple steps  
- Calling APIs and internal tools  
- Maintaining context across the full ticket lifecycle  

### Key Concepts Demonstrated
- **Multi-Agent Pipeline:**  
  Classifier → Summarizer → Response Generator → QA Validator → Publisher

- **Tool Use:**  
  Mock ticket API, knowledge base search, structured output validation

- **Sessions & State:**  
  Ticket-level context tracking with memory

- **Long-Term Memory:**  
  Stores recurring issue signatures & historical customer patterns

- **Observability:**  
  Structured logs, traces, and evaluation pipeline

---

## 3. Architecture

SupportGen uses a sequential multi-agent design:

1. **Ingestion Agent** — retrieves new tickets  
2. **Classifier Agent** — predicts category and priority  
3. **Summarizer Agent** — generates concise TL;DR summaries  
4. **Responder Agent** — drafts responses from knowledge base  
5. **QA Agent** — validates tone, accuracy, and completeness  
6. **Publisher Agent** — sends final response & updates ticket status  

**Architecture Diagram:**  
Add your diagram to:
```
docs/architecture.png
```

---

## 4. How to Run (Reproducible)

### Prerequisites
- Python 3.10+
- pip

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Start the Mock Ticket API
```bash
python src/tools/mock_ticket_api.py
```

### Run the Demo
```bash
python src/agent.py --demo
```

### Run Evaluation
```bash
python src/eval.py --eval-set data/eval_set.csv
```

---

## 5. Files & Structure

```
supportgen-capstone/
├── README.md
├── report.pdf
├── requirements.txt
├── src/
│   ├── agent.py
│   ├── llm_client.py
│   ├── memory.py
│   ├── logger.py
│   ├── classifiers.py
│   ├── generator.py
│   ├── eval.py
│   └── tools/
│       ├── ticket_adapter.py
│       └── mock_ticket_api.py
├── notebooks/
│   └── demo.ipynb
├── data/
│   ├── sample_complaints.json
│   └── eval_set.csv
├── docs/
│   ├── architecture.png
│   └── metrics.png
├── deploy/
│   ├── Dockerfile
│   └── cloud_run.md
├── tests/
│   └── test_agent.py
├── logs/
│   └── example_log.jsonl
└── scripts/
    └── evaluate.sh
```

---

## 6. Evaluation

### Dataset
Synthetic customer ticket dataset including:
- Refund requests  
- Bug reports  
- Account access issues  
- Billing questions  
- General inquiries  

### Metrics
| Metric | Description | Result |
|--------|-------------|--------|
| Classification Accuracy | Correct ticket category prediction | TBD |
| ROUGE-L | Summary similarity score | TBD |
| Response Quality | Human-rated usefulness | TBD |

Full evaluation report available at:
```
reports/eval_report.json
```

---

## 7. Deployment

### Option A — Docker
```bash
docker build -t supportgen .
docker run -p 8080:8080 supportgen
```

### Option B — Cloud Run
1. Build and push container  
2. Deploy using `gcloud run deploy`  
3. Expose `/ticket` endpoint  

---

## 8. Video
YouTube link: **<paste link here>**

Your video should cover:
- Problem overview  
- Why agents?  
- Architecture explanation  
- Live demo  
- Evaluation summary  
- Deployment walkthrough  

---

## 9. Limitations & Future Work
- Multi-intent tickets may still require human review  
- Knowledge base content must be kept updated  
- Currently supports only English  
- Future improvements:
  - RAG-based retrieval  
  - Automated escalation rules  
  - Multi-language support  
  - Dashboard for analytics & monitoring  

---

## 10. Team
- **Pranav Gaikwad** 
- **Sanchali Torpe** 

---

## 11. License & Credits
This project uses open-source libraries and LLM agent concepts for educational purposes.  
Choose a license for your repo (MIT recommended).
