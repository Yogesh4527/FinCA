# agents/gst_agent.py
"""
FinCA – GST Agent
Handles GST filing, invoice validation, GSTR reconciliation,
HSN code lookup, and Input Tax Credit (ITC) queries.
"""

class GSTAgent:
    """Agent responsible for GST related queries."""

    def __init__(self, llm, retriever=None):
        self.llm = llm
        self.retriever = retriever

    def run(self, query: str, context: list = None) -> str:
        """Process a GST-related query and return a response."""
        # TODO: Implement GST agent logic
        raise NotImplementedError("GSTAgent under development.")
