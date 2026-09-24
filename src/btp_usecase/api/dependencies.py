from __future__ import annotations

from fastapi import Depends

from ..core.config import get_settings
from ..graph.graph import build_graph
from ..services.document_service import DocumentService
from ..storage.local import LocalDocumentStorage


def get_settings_dependency():
    return get_settings()


def get_document_service() -> DocumentService:
    storage = LocalDocumentStorage(base_path=get_settings_dependency().storage_path)
    return DocumentService(storage=storage)


def get_agent_graph():
    return build_graph()
