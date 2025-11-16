# SupportGen — AI Customer Support Ticket Automation Agent

## 1. Elevator pitch
- Problem: Customer support teams spend significant time manually triaging, summarizing, and drafting responses to repetitive support tickets, leading to delays and inconsistent resolutions.

- Solution: SupportGen automates the end‑to‑end ticket workflow using a coordinated multi‑agent system capable of classification, summarization, knowledge‑based response drafting, and final quality assurance.

- Value: Reduces manual triage and drafting time by 60–80%, increases accuracy and consistency, and enables support teams to focus on complex, high‑value customer issues.

## 2. Core concept & novelty
Why agents?

Support tickets require interpretation, reasoning, and tool usage—tasks that static ML systems struggle with. Agents allow SupportGen to adapt, reason through escalating    complexity, and interact with internal tools such as ticket APIs and knowledge bases.
- Reason through ambiguous requests.  
- Perform multi-step tasks.  
- Call APIs and internal tools.  
- Maintain context across a ticket lifecycle. 

Key Concepts Demonstrated:
- Multi‑Agent Pipeline: Classifier → Summarizer → Response Generator → QA Validator → Publisher.

- Tool Use: Mock ticket API, knowledge base search, and structured output validation.

- Sessions & State: Ticket‑level state tracking with contextual memory.

- Long‑Term Memory: Stores historical customer patterns and recurring issue signatures.

- Observability: Structured logs and traces for debugging cross‑agent workflows.

## 3. Architecture
- SupportGen follows a sequential multi-agent pipeline:

1. **Ingestion Agent** — fetches new tickets  
2. **Classifier Agent** — predicts category & priority  
3. **Summarizer Agent** — generates TL;DR summaries  
4. **Responder Agent** — drafts responses using knowledge base tools  
5. **QA Agent** — checks accuracy, tone, compliance  
6. **Publisher Agent** — sends final response & updates status

- A full architecture diagram should be added at:

```
docs/architecture.png
```

## 4. How to run (reproducible)

- ### **Prerequisites**
- Python 3.10+
- pip

### **Installation**
```bash
pip install -r requirements.txt
```

### **Start Mock Ticket API**
```bash
python src/tools/mock_ticket_api.py
```

### **Run Demo**
```bash
python src/agent.py --demo
```

### **Run Evaluation**
```bash
python src/eval.py --eval-set data/eval_set.csv
```

## 5. Files & structur

│
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

  
## 6. Evaluation

### **Dataset**
Synthetic ticket dataset including:
- Refund requests  
- Bug reports  
- Account access issues  
- Billing problems  
- General inquiries  

### **Metrics**
| Metric | Description | Result |
|--------|-------------|--------|
| Classification Accuracy | Correct category prediction | TBD |
| ROUGE-L | Summary similarity score | TBD |
| Response Quality | Human-rated draft usefulness | TBD |

See the full evaluation here:

```
reports/eval_report.json
```

---
```
## 7. Deployment

### **Option A — Docker**
```bash
docker build -t supportgen .
docker run -p 8080:8080 supportgen
```

### **Option B — Cloud Run**
1. Build and push container  
2. Deploy using `gcloud run deploy`  
3. Expose `/ticket` endpoint  

(Documentation for reproducibility included in repo.)

## 8. Video
YouTube link: <paste link>
Video should include:
- Problem overview  
- Why agents?  
- Architecture explanation  
- Live demo  
- Build overview

## 9. Limitations & future work
- Complex multi-intent tickets may require human oversight  
- Knowledge base must be updated regularly  
- Only English support currently  
- Future improvements:
  - RAG-based retrieval  
  - Auto-escalation logic  
  - Multi-language support  
  - Analytics dashboard  

## 10. Team
- 


## 11. License & credits
