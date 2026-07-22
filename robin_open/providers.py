"""Optional workers for OpenAI-compatible chat-completions endpoints."""
from __future__ import annotations

import json
import os
import urllib.request

from .runtime import Candidate, Worker


def openai_compatible_worker(
    name: str,
    *,
    system_prompt: str,
    model: str | None = None,
    base_url: str | None = None,
    api_key: str | None = None,
    timeout: float = 45.0,
) -> tuple[str, Worker]:
    """Create a worker for OpenAI-compatible ``/chat/completions`` APIs.

    Credentials are read at runtime from ``ROBIN_OPEN_API_KEY`` when omitted.
    Nothing is persisted or emitted in workflow events.
    """
    endpoint = (base_url or os.environ.get("ROBIN_OPEN_BASE_URL", "https://api.openai.com/v1")).rstrip("/")
    selected_model = model or os.environ.get("ROBIN_OPEN_MODEL", "gpt-4o-mini")
    token = api_key or os.environ.get("ROBIN_OPEN_API_KEY")
    if not token:
        raise ValueError("set ROBIN_OPEN_API_KEY before creating an OpenAI-compatible worker")

    def worker(task: str) -> Candidate:
        payload = json.dumps({
            "model": selected_model,
            "temperature": 0.2,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": task},
            ],
        }).encode("utf-8")
        request = urllib.request.Request(
            f"{endpoint}/chat/completions",
            data=payload,
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = json.load(response)
        value = body["choices"][0]["message"]["content"].strip()
        return Candidate(value=value, score=1.0, worker=name, rationale=f"model={selected_model}")

    return name, worker
