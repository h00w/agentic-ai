---
license: cc-by-4.0
task_categories:
  - text-classification
  - question-answering
  - text-generation
language:
  - en
tags:
  - agentic-ai
  - ai-agents
  - evaluation
  - ai-safety
  - prompt-injection
  - rag
  - tool-use
  - multi-agent
  - trustworthy-ai
  - ai-governance
pretty_name: Hendar Agentic AI Evaluation & Security Benchmark
size_categories:
  - n<1K
configs:
  - config_name: task_success
    data_files: data/task_success.jsonl
  - config_name: tool_routing
    data_files: data/tool_routing.jsonl
  - config_name: rag_groundedness
    data_files: data/rag_groundedness.jsonl
  - config_name: prompt_injection
    data_files: data/prompt_injection.jsonl
  - config_name: unsafe_tool_requests
    data_files: data/unsafe_tool_requests.jsonl
  - config_name: policy_decisions
    data_files: data/policy_decisions.jsonl
  - config_name: multi_agent_tasks
    data_files: data/multi_agent_tasks.jsonl
  - config_name: regression_cases
    data_files: data/regression_cases.jsonl
---

# Hendar Agentic AI Evaluation & Security Benchmark

A compact, expert-authored benchmark for evaluating **trustworthy agentic AI systems** across capability, tool use, retrieval, security, policy enforcement, multi-agent coordination and regression safety. The current release contains **104 synthetic cases: 13 cases in each of 8 domains**.

This dataset is a public companion to the [Agentic AI Academy](https://github.com/h00w/agentic-ai) by **Hendar Mawan, PhD**. It is designed for evaluation, CI regression testing, red-team exercises and engineering education—not as a generic instruction-tuning corpus.

## Benchmark domains

| Config | Purpose | Core signal |
|---|---|---|
| `task_success` | Goal completion | whether the agent reaches the requested outcome within constraints |
| `tool_routing` | Tool selection | whether the correct tool is selected or tools are avoided |
| `rag_groundedness` | Retrieval quality | citation/evidence fidelity and unsupported-claim resistance |
| `prompt_injection` | Injection defense | whether untrusted instructions are ignored and reported |
| `unsafe_tool_requests` | Action safety | whether destructive, privacy-invasive or unauthorized actions are blocked |
| `policy_decisions` | Governance | allow / require-approval / deny classification with rationale |
| `multi_agent_tasks` | Coordination | delegation, role boundaries, aggregation and conflict handling |
| `regression_cases` | Release gating | stable cases intended to catch known classes of engineering regressions |

## Common schema

Every record contains:

- `id` — stable benchmark identifier
- `domain` — benchmark domain
- `input` — user/task input
- `context` — optional system, retrieved or organizational context
- `expected` — expected behavior or output properties
- `expected_label` — compact machine-checkable target
- `risk_level` — `low`, `medium`, `high`, or `critical`
- `tags` — scenario labels for slicing results
- `rationale` — why the expected behavior is correct

Some configs add domain-specific fields such as `candidate_tools`, `evidence`, `attack_type`, `policy`, `agents`, or `regression_target`.

## Intended uses

Use the benchmark to test agent controllers, policy engines, tool routers, RAG pipelines, approval gates, prompt-injection defenses, multi-agent supervisors and CI/CD release gates. It is deliberately small enough to inspect manually and structured enough to automate.

A recommended evaluation report includes **task success, routing accuracy, groundedness, injection-defense pass rate, unsafe-action block rate, policy-decision accuracy, coordination success and regression pass rate**.

## Limitations

The benchmark is synthetic and expert-authored. It does not represent all real-world threats, languages, industries or adversarial strategies. Passing it is evidence of implementation quality, not proof of complete safety or compliance. High-risk systems require domain-specific threat modeling, independent testing and operational controls.

## Provenance and privacy

All cases are synthetic. No private customer data, credentials or production secrets are included. Examples that mention sensitive resources use fictional identifiers.

## Related resources

- Academy: https://hendarmawan.se/agentic-ai/
- GitHub: https://github.com/h00w/agentic-ai
- Interactive Playground: https://huggingface.co/spaces/h0000w/hendar-agentic-ai
- Author: https://hendarmawan.se/

## Citation

If you use this benchmark in teaching, evaluation or research, cite the Agentic AI Academy repository and dataset URL.

## License

Benchmark data: **CC BY 4.0**. Canonical Academy source code remains under its repository license.


## Five-level production-AI proof

The Academy now uses the shared proof model:

`L1 Runnable → L2 Reproducible → L3 Capability-Validated → L4 Production-Candidate → L5 Production-Validated`.

The public Playground and benchmark Dataset support the independently inspectable capability layer. The canonical GitHub source computes the current level with `make proof`; this project deliberately caps its claim at **L3 — Capability-Validated** and does not infer production deployment from a demo.

Specification: https://github.com/h00w/agentic-ai/blob/main/PROOF_MODEL.md
