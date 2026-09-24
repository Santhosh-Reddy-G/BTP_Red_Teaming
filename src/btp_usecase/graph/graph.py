from __future__ import annotations

from langgraph.graph import END, StateGraph

from .nodes.api import external_api_call
from .nodes.document import retrieve_document
from .nodes.input import normalize_query
from .nodes.llm import llm_process
from .nodes.response import finalize_response
from .state import AgentState


def build_graph():
    workflow = StateGraph(AgentState)
    workflow.add_node("input", normalize_query)
    workflow.add_node("document", retrieve_document)
    workflow.add_node("llm", llm_process)
    workflow.add_node("api", external_api_call)
    workflow.add_node("response", finalize_response)

    workflow.set_entry_point("input")
    workflow.add_edge("input", "document")
    workflow.add_edge("document", "llm")
    workflow.add_edge("llm", "api")
    workflow.add_edge("api", "response")
    workflow.add_edge("response", END)

    return workflow.compile()
