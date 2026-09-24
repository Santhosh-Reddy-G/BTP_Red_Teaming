from __future__ import annotations

from ..state import AgentState


def retrieve_document(state: AgentState) -> AgentState:
    document_text = state.get("document_text")
    state["retrieved_context"] = [document_text] if document_text else []
    state["intermediate_results"] = {"retrieval": {"document_id": state.get("document_id")}}
    return state
