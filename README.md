# 🧾 FinCA – Multi-Agent Generative AI for CA Task Automation

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active%20Development-brightgreen" />
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
  <img src="https://img.shields.io/badge/LangGraph-Multi--Agent-purple" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688" />
  <img src="https://img.shields.io/badge/React-Frontend-61DAFB" />
</p>

> **FinCA** is an open-source Multi-Agent Generative AI system designed to automate Chartered Accountant (CA) workflows — making professional-grade financial intelligence accessible to small businesses, startups, and individuals across India who cannot afford CA services.

---

## 🎯 Problem Statement

In India, over **63 million MSMEs** and countless individuals struggle with:
- Complex **GST filing** and compliance
- **Income Tax** computation and ITR filing
- **Audit preparation** and documentation
- Accessing **financial advisory** without expensive CA fees

FinCA bridges this gap using Generative AI and multi-agent reasoning.

---

## ✨ Features

| Agent | Capability |
|-------|-----------|
| 🧮 **Tax Agent** | Income tax computation, ITR guidance, deduction optimization |
| 📦 **GST Agent** | GST filing, invoice validation, GSTR reconciliation |
| 🔍 **Audit Agent** | Automated audit checklists, document review, anomaly detection |
| 📋 **Compliance Agent** | Regulatory deadline tracking, MCA filings, ROC compliance |
| 💡 **Financial Advisory Agent** | Investment insights, cash flow analysis, financial planning |

---

## 🏗️ Architecture

```
User Query
    │
    ▼
┌─────────────────────────────────────────┐
│           LangGraph Orchestrator         │
│  (Multi-Agent Coordination & Routing)   │
└──────────┬──────────────────────────────┘
           │
    ┌──────▼──────┐
    │  RAG Layer  │  ◄── ChromaDB / Pinecone (IT Act, GST Act, ICAI Standards)
    └──────┬──────┘
           │
  ┌────────▼────────┐
  │  Specialized    │
  │  AI Agents      │  ◄── GPT-4o / Gemini Pro
  └────────┬────────┘
           │
  ┌────────▼────────┐
  │  FastAPI Backend│
  └────────┬────────┘
           │
  ┌────────▼────────┐
  │  React Frontend │
  └─────────────────┘
```

---

## 🛠️ Tech Stack

### Backend
- **LangGraph** – Multi-agent orchestration and state management
- **LangChain** – Agent tooling, prompt management, chains
- **FastAPI** – REST API backend
- **ChromaDB / Pinecone** – Vector database for hybrid RAG
- **XGBoost** – ML-based anomaly detection for audit

### AI Models
- **GPT-4o** (OpenAI) – Primary reasoning engine
- **Gemini Pro** (Google) – Secondary model / fallback

### Frontend
- **React.js** – User interface
- **Tailwind CSS** – Styling

### Infrastructure
- **Python 3.10+**
- **Docker** (planned)
- **PostgreSQL** – Structured data storage

---

## 📁 Project Structure

```
FinCA/
├── agents/
│   ├── tax_agent.py
│   ├── gst_agent.py
│   ├── audit_agent.py
│   ├── compliance_agent.py
│   └── advisory_agent.py
├── orchestrator/
│   └── langgraph_orchestrator.py
├── rag/
│   ├── embeddings.py
│   ├── retriever.py
│   └── vector_store.py
├── api/
│   ├── main.py
│   └── routes/
├── frontend/
│   └── src/
├── data/
│   └── knowledge_base/   # IT Act, GST Act, ICAI docs
├── models/
│   └── anomaly_detector.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Node.js 18+
- OpenAI API Key or Google Gemini API Key

### Installation

```bash
# Clone the repository
git clone https://github.com/Yogesh4527/FinCA.git
cd FinCA

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your API keys

# Start the backend
uvicorn api.main:app --reload

# Start the frontend (in a new terminal)
cd frontend
npm install
npm start
```

---

## 🌍 Impact

FinCA is built for **India's underserved financial ecosystem**:
- 🏪 Small shop owners who can't afford a CA
- 🚀 Startups navigating GST and compliance for the first time
- 👨‍🌾 Freelancers and gig workers filing ITR independently
- 🏥 NGOs handling compliance without dedicated finance teams

---

## 🗺️ Roadmap

- [x] Project architecture and planning
- [x] KSCST SPP Synopsis submission
- [ ] Core agent development (Tax + GST)
- [ ] RAG pipeline with Indian tax law documents
- [ ] FastAPI backend
- [ ] React frontend
- [ ] Audit and Compliance agents
- [ ] Full integration and testing
- [ ] Public beta release

---

## 🤝 Contributing

Contributions are welcome! This project is open-source and community-driven.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Yogesh Meda**
- GitHub: [@Yogesh4527](https://github.com/Yogesh4527)
- Project: KSCST Student Projects Programme (49th Series) — Theme 6: AI, Data Engineering & Robotics

---

## 🙏 Acknowledgements

- [LangChain](https://langchain.com/) and [LangGraph](https://langchain-ai.github.io/langgraph/) for the agent framework
- [Anthropic Claude](https://claude.ai/) for AI assistance during development
- KSCST for supporting student innovation in AI

---

<p align="center">Made with ❤️ for India's financial ecosystem</p>
