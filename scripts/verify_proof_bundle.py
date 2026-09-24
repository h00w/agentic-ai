"""Verify the portable Production AI proof bundle without trusting mutable repository state."""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import tarfile
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]


def sha256(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def safe_extract(tar: tarfile.TarFile, target: pathlib.Path) -> None:
    target_resolved = target.resolve()
    for member in tar.getmembers():
        if member.issym() or member.islnk():
            raise ValueError(f"links_not_allowed:{member.name}")
        destination = (target / member.name).resolve()
        if destination != target_resolved and target_resolved not in destination.parents:
            raise ValueError(f"path_traversal:{member.name}")
    tar.extractall(target)


def safe_manifest_path(root: pathlib.Path, relative_path: str) -> pathlib.Path:
    candidate = pathlib.Path(relative_path)
    if candidate.is_absolute():
        raise ValueError(f"absolute_path_not_allowed:{relative_path}")
    resolved = (root / candidate).resolve()
    root_resolved = root.resolve()
    if resolved != root_resolved and root_resolved not in resolved.parents:
        raise ValueError(f"path_traversal:{relative_path}")
    return resolved


def validate_manifest_entry(item: object, index: int) -> tuple[str, str, int] | None:
    if not isinstance(item, dict):
        raise ValueError(f"malformed_entry:{index}")
    path = item.get("path")
    sha256_value = item.get("sha256")
    byte_count = item.get("bytes")
    if not isinstance(path, str) or not isinstance(sha256_value, str) or not isinstance(
        byte_count, int
    ):
        raise ValueError(f"malformed_entry:{index}")
    return path, sha256_value, byte_count


def verify_bundle(bundle: pathlib.Path) -> dict:
    errors: list[str] = []
    with tempfile.TemporaryDirectory() as tmp:
        target = pathlib.Path(tmp)
        with tarfile.open(bundle, "r:gz") as tar:
            safe_extract(tar, target)

        manifest_path = target / "evidence" / "out" / "current" / "proof-manifest.json"
        if not manifest_path.is_file():
            errors.append("missing:proof-manifest.json")
        else:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            for index, item in enumerate(manifest.get("files", [])):
                try:
                    relative_path, sha256_value, byte_count = validate_manifest_entry(
                        item, index
                    )
                except ValueError as exc:
                    errors.append(str(exc))
                    continue
                try:
                    path = safe_manifest_path(target, relative_path)
                except ValueError as exc:
                    errors.append(str(exc))
                    continue
                if not path.is_file():
                    errors.append(f"missing:{relative_path}")
                elif sha256(path) != sha256_value:
                    errors.append(f"sha256_mismatch:{relative_path}")
                elif path.stat().st_size != byte_count:
                    errors.append(f"size_mismatch:{relative_path}")

    return {
        "verified": not errors,
        "bundleSha256": sha256(bundle),
        "errors": errors,
        "signatureVerification": "not_performed",
        "next": "Use gh attestation verify <bundle> -R OWNER/REPO to verify the external GitHub/Sigstore attestation.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "bundle", nargs="?", default="evidence/out/current/production-ai-proof-bundle.tar.gz"
    )
    args = parser.parse_args()
    bundle = pathlib.Path(args.bundle)
    if not bundle.is_absolute():
        bundle = ROOT / bundle

    result = verify_bundle(bundle)
    print(json.dumps(result, indent=2))
    return 0 if result["verified"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
