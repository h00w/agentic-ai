from pydantic import BaseModel, Field


class SearchArguments(BaseModel):
    query: str = Field(min_length=3)
    limit: int = Field(default=3, ge=1, le=10)


def search(arguments: SearchArguments) -> list[str]:
    corpus = ["RAG grounds answers in retrieved evidence.", "Policy gates bound tool use.", "Evaluation detects regressions."]
    return corpus[: arguments.limit]


request = SearchArguments(query="agent reliability", limit=2)
print(search(request))
