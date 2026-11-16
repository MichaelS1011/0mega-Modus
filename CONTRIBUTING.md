# Contributing to ØMEGA Modus

Thank you for helping improve ØMEGA Modus. Contributions should make the framework more reliable, clearer, safer, more portable, or easier to evaluate.

## Before opening a pull request

1. Open or review an issue describing the problem and proposed change.
2. Keep platform-neutral rules in `skills/omega-modus/references/`.
3. Keep provider-specific syntax in `adapters/` or in `scripts/build_release.py` templates.
4. Avoid platform claims that are not supported by current vendor documentation.
5. Do not add instructions asking models to reveal private chain-of-thought.
6. Add or update evaluation scenarios when behavior changes.

## Required checks

```bash
python scripts/build_release.py
python scripts/validate_release.py
python -m unittest discover -s tests -v
```

## Pull request description

Include:
- Problem being addressed.
- Behavior before and after the change.
- Platforms affected.
- Evaluation scenario(s) added or updated.
- Any known limitations.

## Design principles

- Proportionate rigor: do not over-process simple tasks.
- Evidence over confidence: do not label assumptions as facts.
- Safety by design: prefer reversibility, least privilege, and clear approvals.
- Truthful verification: distinguish executed checks from proposed checks.
- Portability: the canonical protocol must not depend on one model vendor.
- Accessibility: use clear language and minimize unnecessary jargon.
