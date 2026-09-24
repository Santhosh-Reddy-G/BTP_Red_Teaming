from __future__ import annotations

from ..state import AgentState


def finalize_response(state: AgentState) -> AgentState:
    if not state.get("final_response"):
        state["final_response"] = "I could not generate a response."
    return state
