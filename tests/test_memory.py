from agentic_ai import MemoryStore


def test_memory_search():
    store = MemoryStore(["RAG retrieves evidence", "Policy restricts tools"])
    assert store.search("retrieve evidence") == ["RAG retrieves evidence"]
