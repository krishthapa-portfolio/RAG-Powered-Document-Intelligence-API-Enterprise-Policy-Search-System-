# 📄 RAG-Powered Document Intelligence API (Enterprise Policy Search System)

## 🚀 Overview

This project is a production-style Retrieval-Augmented Generation (RAG) system designed to simulate how employees can query internal company policy documents using natural language.

Instead of manually searching PDFs or policy handbooks, employees can ask questions such as:

- “What is the vacation policy?”
- “What happens in case of workplace injury?”
- “What is the reimbursement policy?”

The system retrieves relevant sections from uploaded company documents and uses an LLM to generate accurate, context-grounded answers.

Built as a backend-first AI system with production-style API design, security controls, and structured validation.

---

## 🧠 How It Works

Company Policy PDF → Chunking → Embeddings → Vector DB (ChromaDB)
↓
User Question → Semantic Search → Relevant Policy Sections
↓
Groq LLM (Llama 3) → Final Answer
↓
Secure API Response

---

## ⚙️ Tech Stack

- FastAPI (REST API backend)
- LangChain (RAG orchestration)
- ChromaDB (vector database)
- HuggingFace Embeddings (semantic search)
- Groq LLM (Llama 3 inference)
- Pydantic (input validation)
- python-dotenv (.env security management)

---

## 🔐 Security & Production Design

- API key authentication via request headers
- Pydantic schema validation for safe input handling
- Environment variable protection for secrets (.env)
- Structured REST API endpoints for scalable deployment

---

## 💼 Business Value

This system demonstrates how enterprises can:

- Reduce time spent searching internal documentation
- Improve employee access to HR and compliance policies
- Standardize knowledge retrieval across departments
- Enable AI-driven internal knowledge assistants