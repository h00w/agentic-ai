import streamlit as st

st.set_page_config(page_title="Agentic AI Learning Lab", page_icon="🧭", layout="wide")
st.title("Agentic AI Academy — Learning Lab")
st.caption("Engineering trustworthy AI agents from learning to production. — Hendar Mawan, PhD")

goal = st.text_input("Goal", "Evaluate whether a research agent should use a database-write tool")
autonomy = st.select_slider("Autonomy", ["Suggest only", "Approval required", "Low-risk autonomous"], value="Approval required")
cols = st.columns(3)
cols[0].metric("Task success", "100%")
cols[1].metric("Safety", "100%")
cols[2].metric("Estimated cost", "$0.00")

st.subheader("Agent control plane")
st.code("Goal → Planner → Policy → Tool Gateway → Evidence → Evaluation → Approval → Output → Audit")

if st.button("Run deterministic lab"):
    if "write" in goal.lower() or autonomy == "Approval required":
        st.warning("Policy decision: REQUIRE APPROVAL — no privileged write executed.")
    else:
        st.success("Policy decision: ALLOW — read-only deterministic tool execution.")
    st.json({"goal": goal, "autonomy": autonomy, "trace_events": 6, "external_api_key_required": False})
