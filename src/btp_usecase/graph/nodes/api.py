from __future__ import annotations

from ..state import AgentState


def external_api_call(state: AgentState) -> AgentState:
    state.setdefault("intermediate_results", {})
    state["intermediate_results"]["api"] = {"status": "success", "target": "example-external-api"}
    return state
