# Changelog

All notable changes are documented here.

## v0.2.0 - 2026-07-22

### Added
- `openai_compatible_worker()` for any OpenAI-compatible chat-completions endpoint.
- A zero-key terminal trace demo with candidate scores, an isolated failure, and event flow.
- A real-model example configured only with runtime environment variables.
- Timeout handling that retains completed candidates while recording slow workers as failures.

### Security
- API credentials remain process-local and are never written to workflow events or repository files.

## v0.1.0 - 2026-07-22

- Initial transparent multi-agent runtime with Best-of-N selection and append-only events.
