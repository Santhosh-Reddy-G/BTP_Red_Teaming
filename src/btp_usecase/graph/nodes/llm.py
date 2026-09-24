from __future__ import annotations

from ...core.config import get_settings
from ...llm.base import LLMProvider
from ...llm.factory import get_llm_provider
from ..state import AgentState


def llm_process(state: AgentState) -> AgentState:
    context = "\n".join(state.get("retrieved_context") or [])
    prompt = state.get("user_query") or ""
    settings = get_settings()
    provider: LLMProvider = get_llm_provider(settings)

    if not context:
        response = f"No document context was provided for '{prompt}'."
    else:
        response = provider.generate(prompt=prompt, context=context)

    state["intermediate_results"] = {"llm": {"response": response, "provider": settings.llm_provider, "model": settings.llm_model}}
    state["final_response"] = response
    return state
