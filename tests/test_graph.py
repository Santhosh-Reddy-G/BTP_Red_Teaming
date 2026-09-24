from btp_usecase.graph.graph import build_graph


def test_graph_compiles_and_runs():
    graph = build_graph()
    result = graph.invoke({"user_query": "Summarize the uploaded document", "document_id": "doc-123", "document_text": "This is a test document."})

    assert result["final_response"]
    assert result["document_text"] == "This is a test document."
    assert result["messages"]
