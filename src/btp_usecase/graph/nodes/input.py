from __future__ import annotations

from ..state import AgentState


def normalize_query(state: AgentState) -> AgentState:
    query = (state.get("user_query") or "").strip()
    state["user_query"] = query
    state["messages"] = [query] if query else []
    return state
