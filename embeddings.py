# rag/embeddings.py
"""
FinCA – Embeddings Module
Handles document embedding for the RAG pipeline using
sentence-transformers or OpenAI embeddings.
"""

from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings


def get_embeddings(model_type: str = "openai"):
    """Return the appropriate embedding model."""
    if model_type == "openai":
        return OpenAIEmbeddings(model="text-embedding-3-small")
    elif model_type == "huggingface":
        return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    else:
        raise ValueError(f"Unknown embedding model type: {model_type}")
