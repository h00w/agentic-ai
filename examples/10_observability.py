from agentic_ai import TraceRecorder

trace = TraceRecorder()
trace.record("plan", "decompose research task")
trace.record("tool", "search: mock corpus")
trace.record("evaluation", "groundedness=1.0")
for event in trace.as_dicts():
    print(event)
