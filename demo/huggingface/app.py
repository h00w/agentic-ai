from __future__ import annotations

import gradio as gr


def run_demo(goal: str, autonomy: str, enable_write: bool):
    """Run a deterministic agent simulation without external API keys."""
    goal = (goal or "Research trustworthy AI agents").strip()
    plan = [
        "1. Classify task",
        "2. Select approved tool",
        "3. Gather deterministic evidence",
        "4. Evaluate",
        "5. Stop safely",
    ]
    risky = any(
        word in goal.lower()
        for word in ["export", "delete", "send all", "production write", "secret"]
    )
    if risky or enable_write:
        decision = "BLOCKED / APPROVAL REQUIRED"
        result = (
            "High-impact action was not executed. The demo enforces least privilege "
            "and requires explicit approval."
        )
    else:
        decision = "ALLOW: read-only research"
        result = (
            "Trustworthy agents combine bounded autonomy, explicit tool permissions, "
            "evaluation, observability, and governance."
        )

    trace = "\n".join(
        [
            f"goal: {goal}",
            f"autonomy: {autonomy}",
            f"policy: {decision}",
            "tool: deterministic knowledge lookup",
            "evaluation: groundedness=1.00",
            "stop: success",
        ]
    )
    metrics = {
        "task_success": 1.0,
        "groundedness": 1.0,
        "safety": 1.0,
        "tool_accuracy": 1.0,
        "estimated_cost_usd": 0.0,
    }
    return "\n".join(plan), decision, result, metrics, trace


with gr.Blocks(title="Agentic AI Academy") as demo:
    gr.Markdown(
        """# Agentic AI Academy
### Engineering trustworthy AI agents from learning to production.
**By Hendar Mawan, PhD**"""
    )
    goal = gr.Textbox(label="Goal", value="Research the principles of trustworthy AI agents")
    autonomy = gr.Radio(
        ["Suggest only", "Execute with approval", "Autonomous low-risk only"],
        value="Autonomous low-risk only",
        label="Autonomy",
    )
    enable_write = gr.Checkbox(label="Request a privileged write action (security test)")
    run = gr.Button("Run Agent")
    plan = gr.Textbox(label="Plan")
    policy = gr.Textbox(label="Policy decision")
    result = gr.Textbox(label="Result")
    metrics = gr.JSON(label="Evaluation")
    trace = gr.Textbox(label="Trace")
    run.click(
        run_demo,
        [goal, autonomy, enable_write],
        [plan, policy, result, metrics, trace],
    )


if __name__ == "__main__":
    demo.launch()
