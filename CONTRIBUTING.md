# Contributing to Robin Open

Thanks for helping make agent systems more transparent and useful.

## Before opening a PR

1. Explain the user problem and the smallest change that solves it.
2. Add or update tests for behavior changes.
3. Run `pytest` and `python -m compileall robin_open`.
4. Keep dependencies optional unless they are essential to the core.
5. Never include secrets, private data, generated artifacts, or competition deliverables.

## Design principles

- Prefer explicit control flow over hidden magic.
- Preserve event traces and failure context.
- Make local execution possible.
- Keep model/provider integrations behind small interfaces.
- Document tradeoffs and security boundaries.
