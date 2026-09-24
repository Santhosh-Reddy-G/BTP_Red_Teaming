from __future__ import annotations

from typing import TypedDict, Any


class AgentState(TypedDict, total=False):
    user_query: str
    document_id: str | None
    document_text: str | None
    retrieved_context: list[str]
    messages: list[str]
    intermediate_results: dict[str, Any]
    final_response: str | None
