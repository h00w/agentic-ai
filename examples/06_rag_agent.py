from dataclasses import dataclass


@dataclass(frozen=True)
class Document:
    source: str
    text: str


docs = [
    Document("security.md", "Agents should use explicit tool permissions and approval gates."),
    Document(
        "evaluation.md",
        "Agent evaluation should measure task success, groundedness, safety, latency and cost.",
    ),
]
query = "How should agents be evaluated?"
terms = set(query.lower().replace("?", "").split())
ranked = sorted(
    docs, key=lambda d: sum(term in d.text.lower() for term in terms), reverse=True
)
best = ranked[0]
print(f"Answer: {best.text}\nCitation: {best.source}")
