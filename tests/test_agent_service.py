from btp_usecase.services.agent_service import AgentService
from btp_usecase.storage.local import LocalDocumentStorage


def test_agent_service_reads_document_from_storage(tmp_path):
    storage = LocalDocumentStorage(base_path=tmp_path / "documents")
    storage.save("doc-456", b"This is a stored document for graph testing.")

    service = AgentService(storage=storage)
    result = service.run_agent(user_query="Summarize the stored document", document_id="doc-456")

    assert result["document_id"] == "doc-456"
    assert "document_text" not in result
    assert result["final_response"]
