from __future__ import annotations

import os
from pathlib import Path

from huggingface_hub import HfApi


SPACE_REPO = os.environ.get("HF_SPACE_REPO", "h0000w/hendar-agentic-ai")
TOKEN = os.environ.get("HF_TOKEN")
SOURCE = Path("deploy/huggingface")


def main() -> None:
    if not TOKEN:
        raise RuntimeError("HF_TOKEN is required")
    if not SOURCE.exists():
        raise RuntimeError(f"Missing Space source directory: {SOURCE}")

    api = HfApi(token=TOKEN)
    api.create_repo(
        repo_id=SPACE_REPO,
        repo_type="space",
        space_sdk="gradio",
        private=False,
        exist_ok=True,
    )
    api.upload_folder(
        repo_id=SPACE_REPO,
        repo_type="space",
        folder_path=str(SOURCE),
        commit_message="Deploy Agentic AI Playground from canonical GitHub source",
    )
    print(f"Published https://huggingface.co/spaces/{SPACE_REPO}")


if __name__ == "__main__":
    main()
