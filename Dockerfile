FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY pyproject.toml README.md ./
COPY src ./src
RUN pip install --no-cache-dir .
USER nobody
CMD ["python", "-c", "from agentic_ai import MemoryStore; print('agentic-ai health: ok')"]
