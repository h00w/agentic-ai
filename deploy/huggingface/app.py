from __future__ import annotations

import ast
import operator
from dataclasses import dataclass
from time import perf_counter

import gradio as gr


@dataclass(frozen=True)
class Tool:
    name: str
    description: str
    risk: str


TOOLS = {
    "research": Tool("research", "Retrieve grounded Academy knowledge", "low"),
    "calculator": Tool("calculator", "Evaluate bounded arithmetic", "low"),
    "deploy": Tool("deploy", "Simulate a production deployment action", "high"),
}

KNOWLEDGE = {
    "evaluation": "Evaluate agents on task success, correctness, groundedness, tool accuracy, safety, latency and cost.",
    "security": "Use least privilege, explicit tool permissions, validation, approval gates, sandbox boundaries and audit logging.",
    "rag": "RAG should retrieve evidence, preserve provenance and make grounded citations available to the agent and evaluator.",
    "observability": "Capture traces, tool calls, policy decisions, latency, failures, token or cost signals and outcome metrics.",
    "governance": "Production governance needs risk ownership, deployment gates, evidence, incident handling and rollback paths.",
    "architecture": "Enterprise agent architecture separates identity, orchestration, model access, tool gateways, knowledge, policy, evaluation and audit.",
}

_ALLOWED_BINOPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}
_ALLOWED_UNARY = {ast.UAdd: operator.pos, ast.USub: operator.neg}


def safe_calculate(expression: str) -> float:
    """Evaluate arithmetic without eval(), names, imports or function calls."""

    def walk(node: ast.AST) -> float:
        if isinstance(node, ast.Expression):
            return walk(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, int | float):
            return float(node.value)
        if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED_BINOPS:
            left = walk(node.left)
            right = walk(node.right)
            if isinstance(node.op, ast.Pow) and abs(right) > 8:
                raise ValueError("Exponent too large for this bounded demo")
            return _ALLOWED_BINOPS[type(node.op)](left, right)
        if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED_UNARY:
            return _ALLOWED_UNARY[type(node.op)](walk(node.operand))
        raise ValueError("Only bounded arithmetic is allowed")

    tree = ast.parse(expression, mode="eval")
    return walk(tree)


def select_tool(goal: str) -> str:
    lowered = goal.lower()
    if any(word in lowered for word in ("deploy", "publish", "release to production")):
        return "deploy"
    if any(ch.isdigit() for ch in goal) or "calculate" in lowered:
        return "calculator"
    return "research"


def policy_decision(tool_name: str, require_approval: bool) -> tuple[str, str]:
    tool = TOOLS[tool_name]
    if tool.risk == "high":
        return "REQUIRE_APPROVAL", "High-risk action requires a human approval gate."
    if require_approval:
        return "REQUIRE_APPROVAL", "Demo policy is configured to require approval for tool execution."
    return "ALLOW", "Tool is permitted under the current bounded demo policy."


def research(query: str) -> tuple[str, str]:
    lowered = query.lower()
    ranked = sorted(
        KNOWLEDGE.items(),
        key=lambda item: sum(term in item[0] or term in item[1].lower() for term in lowered.split()),
        reverse=True,
    )
    topic, answer = ranked[0]
    return answer, f"Academy knowledge: {topic}"


def run_playground(goal: str, require_approval: bool):
    goal = (goal or "").strip()
    if not goal:
        return "Enter a goal to run the agent.", [], "No execution", "—"

    started = perf_counter()
    trace: list[list[str]] = [["1", "goal", goal]]

    tool_name = select_tool(goal)
    trace.append(["2", "plan", f"Selected tool: {tool_name}"])

    decision, rationale = policy_decision(tool_name, require_approval)
    trace.append(["3", "policy", f"{decision} — {rationale}"])

    if decision != "ALLOW":
        elapsed = (perf_counter() - started) * 1000
        answer = f"Human approval required before `{tool_name}` can execute."
        trace.append(["4", "stop", "Execution paused at the policy gate"])
        return answer, trace, decision, f"{elapsed:.2f} ms"

    if tool_name == "calculator":
        expression = "".join(ch for ch in goal if ch in "0123456789.+-*/()% ")
        try:
            result = safe_calculate(expression)
            answer = f"Calculated result: {result:g}"
            citation = "Bounded local calculator"
        except Exception as exc:  # user-facing teaching demo
            answer = f"Calculator rejected the expression: {exc}"
            citation = "Safety boundary triggered"
    elif tool_name == "research":
        answer, citation = research(goal)
    else:
        answer = "Deployment simulation reached the action boundary. A real production system would require explicit approval and environment-specific controls."
        citation = "Simulated deployment boundary"

    trace.append(["4", "tool", f"{tool_name} completed"])
    trace.append(["5", "evidence", citation])
    trace.append(["6", "complete", answer])
    elapsed = (perf_counter() - started) * 1000
    return answer, trace, decision, f"{elapsed:.2f} ms"


def evaluate_answer(answer: str, evidence_present: bool, policy_passed: bool):
    answer = (answer or "").strip()
    completeness = 1.0 if len(answer) >= 60 else 0.6 if answer else 0.0
    groundedness = 1.0 if evidence_present else 0.4
    safety = 1.0 if policy_passed else 0.0
    overall = round((completeness + groundedness + safety) / 3, 2)
    rows = [
        ["Completeness", completeness, "Heuristic demo score based on answer substance"],
        ["Groundedness", groundedness, "Rewards explicit supporting evidence"],
        ["Policy compliance", safety, "Requires policy gate success"],
        ["Overall", overall, "Mean of demo metrics"],
    ]
    return rows, f"Demo evaluation score: {overall:.2f} / 1.00"


CSS = """
.gradio-container {max-width: 1180px !important; margin: auto !important;}
.hero {padding: 28px 30px; border-radius: 24px; background: linear-gradient(135deg, rgba(35,60,90,.08), rgba(80,120,160,.03)); border: 1px solid rgba(100,130,160,.18); margin-bottom: 22px;}
.hero h1 {font-size: 2.2rem; margin-bottom: 6px;}
.hero p {font-size: 1.02rem; line-height: 1.65;}
"""

with gr.Blocks(title="Agentic AI Playground", css=CSS, theme=gr.themes.Soft()) as demo:
    gr.HTML(
        """
        <div class='hero'>
          <h1>Agentic AI Playground</h1>
          <p><strong>Engineering trustworthy AI agents from learning to production.</strong><br>
          Explore planning, tool selection, policy gates, bounded execution, evidence and evaluation in a transparent teaching environment.</p>
          <p>Agentic AI Academy · Hendar Mawan, PhD · <a href='https://github.com/h00w/agentic-ai' target='_blank'>GitHub</a> · <a href='https://hendarmawan.se/agentic-ai/' target='_blank'>Academy</a></p>
        </div>
        """
    )

    with gr.Tab("Agent Playground"):
        with gr.Row():
            with gr.Column(scale=2):
                goal = gr.Textbox(
                    label="Goal",
                    value="Research how an AI agent should be evaluated before production deployment",
                    lines=3,
                )
                approval = gr.Checkbox(
                    label="Require human approval for every tool call",
                    value=False,
                )
                run = gr.Button("Run bounded agent", variant="primary")
            with gr.Column(scale=1):
                decision = gr.Textbox(label="Policy decision", interactive=False)
                latency = gr.Textbox(label="Latency", interactive=False)

        answer = gr.Markdown(label="Agent answer")
        trace = gr.Dataframe(
            headers=["Step", "Stage", "Detail"],
            datatype=["str", "str", "str"],
            label="Execution trace",
            interactive=False,
            wrap=True,
        )
        run.click(run_playground, [goal, approval], [answer, trace, decision, latency])

        gr.Examples(
            examples=[
                ["Research security controls for production AI agents", False],
                ["Calculate 125 * 8 / 4", False],
                ["Deploy this agent to production", False],
                ["Research observability for multi-agent systems", True],
            ],
            inputs=[goal, approval],
        )

    with gr.Tab("Evaluation Lab"):
        gr.Markdown("### Inspect a simple transparent evaluation gate")
        candidate = gr.Textbox(
            label="Candidate answer",
            lines=5,
            value="The agent should be evaluated for task success, groundedness, tool correctness, policy compliance, latency and operational cost, with trace evidence retained for audit.",
        )
        with gr.Row():
            evidence = gr.Checkbox(label="Supporting evidence is present", value=True)
            policy_ok = gr.Checkbox(label="Policy gate passed", value=True)
        evaluate = gr.Button("Evaluate")
        eval_table = gr.Dataframe(
            headers=["Metric", "Score", "Interpretation"],
            datatype=["str", "number", "str"],
            interactive=False,
            wrap=True,
        )
        eval_summary = gr.Markdown()
        evaluate.click(evaluate_answer, [candidate, evidence, policy_ok], [eval_table, eval_summary])

    with gr.Tab("Architecture"):
        gr.Markdown(
            """
### Trustworthy agent execution path

**User goal → Controller → Planner → Policy Engine → Tool Gateway → Knowledge / Tools → Evaluation → Human Approval (when required) → Response → Audit**

This public playground is intentionally bounded. It demonstrates the controls around an agent rather than hiding them behind an opaque chatbot interface.

**Production principles**

- Least-privilege tool access and explicit policy decisions
- Human approval for high-risk actions
- Retrieval provenance and evidence visibility
- Evaluation before and after deployment
- Traceability, observability and audit records
- Failure containment, rollback and lifecycle governance

Source curriculum: [Agentic AI Academy](https://github.com/h00w/agentic-ai)
            """
        )

    gr.Markdown(
        "---\n**Agentic AI Academy** · EXPLORE • IMPLEMENT • SCALE · MIT licensed teaching reference. This demo does not execute external side effects."
    )

if __name__ == "__main__":
    demo.launch()
