# orchestrator/langgraph_orchestrator.py
"""
FinCA – LangGraph Multi-Agent Orchestrator
Coordinates routing between Tax, GST, Audit, Compliance, and Advisory agents.
"""

from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
import operator


class FinCAState(TypedDict):
    """Shared state passed between all agents."""
    query: str
    agent_type: str
    context: list
    response: str
    history: Annotated[list, operator.add]


def route_query(state: FinCAState) -> str:
    """Route the user query to the appropriate agent."""
    query = state["query"].lower()

    if any(word in query for word in ["tax", "itr", "income", "tds", "deduction"]):
        return "tax_agent"
    elif any(word in query for word in ["gst", "invoice", "gstr", "hsn"]):
        return "gst_agent"
    elif any(word in query for word in ["audit", "balance sheet", "financial statement"]):
        return "audit_agent"
    elif any(word in query for word in ["compliance", "roc", "mca", "deadline"]):
        return "compliance_agent"
    else:
        return "advisory_agent"


def build_graph():
    """Build and compile the LangGraph multi-agent workflow."""
    graph = StateGraph(FinCAState)

    # TODO: Add agent nodes
    # graph.add_node("tax_agent", tax_agent_node)
    # graph.add_node("gst_agent", gst_agent_node)
    # graph.add_node("audit_agent", audit_agent_node)
    # graph.add_node("compliance_agent", compliance_agent_node)
    # graph.add_node("advisory_agent", advisory_agent_node)

    # TODO: Add conditional routing
    # graph.add_conditional_edges("router", route_query, {...})

    return graph


# Placeholder for development
if __name__ == "__main__":
    print("FinCA Orchestrator initialized. Agent nodes coming soon.")
