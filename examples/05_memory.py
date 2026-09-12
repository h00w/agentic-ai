from agentic_ai import MemoryStore

memory = MemoryStore()
memory.add("Least privilege limits the blast radius of tool misuse.")
memory.add("RAG should return source evidence with the answer.")
print(memory.search("tool privilege"))
