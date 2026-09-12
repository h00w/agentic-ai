# Public Demo Deployment

| Resource | Role |
|---|---|
| GitHub `h00w/agentic-ai` | Canonical curriculum/source |
| HF Space `h0000w/hendar-agentic-ai` | Interactive public demo |
| HF Dataset `h0000w/hendar-agentic-ai-dataset` | Evaluation/training/demo data |
| HF Model `h0000w/hendar-agentic-ai` | Model/agent artifacts |
| GitHub Pages | Professional academy website |
| Streamlit | Advanced experimental labs |

Copy `demo/huggingface/` into the Space or configure repository synchronization. The default Space demo is deterministic and requires no API key. Deploy `demo/streamlit/app.py` for the laboratory interface. Add credentials only through the hosting platform secret store. Publish the `/website` directory with GitHub Pages or a Pages build workflow. Keep public demo data synthetic or appropriately licensed.
