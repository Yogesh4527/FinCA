# agents/tax_agent.py
"""
FinCA – Tax Agent
Handles Income Tax computation, ITR guidance, deduction optimization,
TDS queries, and tax planning using RAG over Indian IT Act documents.
"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

TAX_SYSTEM_PROMPT = """
You are an expert Indian Income Tax advisor with deep knowledge of:
- Income Tax Act, 1961
- ITR filing procedures
- Deductions under Section 80C, 80D, 80G, etc.
- TDS provisions
- Capital Gains taxation
- GST basics

Always provide accurate, up-to-date tax guidance. Mention relevant sections.
If unsure, advise the user to consult a certified CA.
"""

TAX_PROMPT = ChatPromptTemplate.from_messages([
    ("system", TAX_SYSTEM_PROMPT),
    ("human", "{query}"),
])


class TaxAgent:
    """Agent responsible for Income Tax related queries."""

    def __init__(self, llm, retriever=None):
        self.llm = llm
        self.retriever = retriever  # RAG retriever for IT Act docs
        self.chain = TAX_PROMPT | self.llm | StrOutputParser()

    def run(self, query: str, context: list = None) -> str:
        """Process a tax-related query and return a response."""
        # TODO: Integrate RAG retrieval
        # context = self.retriever.get_relevant_documents(query)
        return self.chain.invoke({"query": query})


# Placeholder
if __name__ == "__main__":
    print("TaxAgent ready. LLM integration pending.")
