from __future__ import annotations

import os
from pathlib import Path

from huggingface_hub import HfApi  # ruff: noqa: I001

DATASET_REPO = os.environ.get("HF_DATASET_REPO", "h0000w/hendar-agentic-ai-dataset")
TOKEN = os.environ.get("HF_TOKEN")
SOURCE = Path("dataset")


def main() -> None:
    if not TOKEN:
        raise RuntimeError("HF_TOKEN is required")
    if not SOURCE.exists():
        raise RuntimeError(f"Missing dataset source directory: {SOURCE}")

    api = HfApi(token=TOKEN)
    api.create_repo(
        repo_id=DATASET_REPO,
        repo_type="dataset",
        private=False,
        exist_ok=True,
    )
    api.upload_folder(
        repo_id=DATASET_REPO,
        repo_type="dataset",
        folder_path=str(SOURCE),
        commit_message="Publish Agentic AI evaluation and security benchmark",
    )
    print(f"Published https://huggingface.co/datasets/{DATASET_REPO}")


if __name__ == "__main__":
    main()
