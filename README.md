# Comment Summariser

Ask questions to any PDF document using AI.
Built with LangChain + HuggingFace + ChromaDB + Gemini Flash.

## 🏗️ Architecture
PDF → Chunking → Embeddings → ChromaDB → 
Query → Similarity Search → Gemini → Answer

## 🚀 Quick Start
pip install -r requirements.txt
fastapi run main.py

## 💻 Tech Stack
- Python, FastAPI
- LangChain, HuggingFace Transformers
- ChromaDB (vector database)
- Google Gemini Flash (LLM)

## 📸 Demo
screenshot