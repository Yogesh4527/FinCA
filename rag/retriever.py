# rag/retriever.py
"""
FinCA – RAG Retriever
Retrieves relevant chunks from Indian tax law documents
(IT Act, GST Act, ICAI Standards) for agent context.
"""

from langchain_community.vectorstores import Chroma
from rag.embeddings import get_embeddings


def get_retriever(persist_dir: str = "./data/chroma_db", k: int = 5):
    """Load ChromaDB vector store and return a retriever."""
    embeddings = get_embeddings("openai")
    vectorstore = Chroma(
        persist_directory=persist_dir,
        embedding_function=embeddings,
    )
    return vectorstore.as_retriever(search_kwargs={"k": k})
