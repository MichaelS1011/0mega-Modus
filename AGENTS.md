# Repository Guidance

This repository maintains ØMEGA Modus, an instruction framework. Keep the canonical protocol in `skills/omega-modus/` and platform-specific wrappers in `adapters/`.

- Read `CONTRIBUTING.md` before changing the protocol.
- Keep instructions concise, testable, and platform-neutral in the canonical skill.
- Do not ask models to reveal private chain-of-thought. Require concise rationales, evidence, and verifiable outputs instead.
- Do not claim tools, tests, persistence, permissions, or capabilities that the host environment does not provide.
- When changing quality-method routing, update `skills/omega-modus/references/QUALITY_INTELLIGENCE.md` and at least one relevant evaluation scenario.
- Run `python scripts/build_release.py`, `python scripts/validate_release.py`, and `python -m unittest discover -s tests -v` before submitting.
