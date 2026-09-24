from __future__ import annotations

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ...services.agent_service import AgentService
from ...storage.local import LocalDocumentStorage

router = APIRouter()


class AgentRequest(BaseModel):
    user_query: str
    document_id: str | None = None
    document_text: str | None = None


@router.post("/agent/run")
async def run_agent(request: AgentRequest):
    storage = LocalDocumentStorage(base_path="./data/documents")
    service = AgentService(storage=storage)

    try:
        result = service.run_agent(
            user_query=request.user_query,
            document_id=request.document_id,
            document_text=request.document_text,
        )
        return result
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
