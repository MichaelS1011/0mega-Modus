# ØMEGA Modus Architecture

## Design

ØMEGA Modus is an instruction-first framework with a canonical skill package and thin platform adapters. It does not include a model, hosted API, orchestration server, or proprietary runtime.

```text
User request
    |
    v
Task router (QUICK / STANDARD / DEEP)
    |
    v
Seven operating functions
SCAN -> VERIFY -> THINK -> STRATEGIZE -> EXECUTE -> VALIDATE -> REPORT
    |
    +---- Quality Intelligence method router
    |       PDCA / Five Whys / Ishikawa / Poka-Yoke / FMEA
    |       Pareto / A3 / Kaizen / basic QC tools
    |
    +---- Safety and trust controls
    |       least privilege / approval / reversibility / evidence honesty
    |
    v
Natural-language result + relevant evidence + limitations
```

## Components

### Canonical skill

`skills/omega-modus/SKILL.md` contains discovery metadata and the concise activation contract. Supporting reference files contain the full protocol, quality methods, safety boundaries, and workflows. This progressive-disclosure structure avoids putting every detail in every request.

### Platform adapters

Adapters map the same core behavior to the native instruction mechanism of each environment. They are thin on purpose. If adapter-specific instructions conflict with the canonical skill, the core protocol wins unless the host platform's higher-priority rules say otherwise.

### Release builder

`scripts/build_release.py` creates self-contained adapter directories under `dist/omega-modus-v1.0.0/bundles/`, seven platform ZIPs, a complete source ZIP, and SHA-256 checksums. It writes only to its versioned output directory and refuses to remove that directory unless its own generation marker is present. Unrelated files already in `dist/` are preserved. The builder uses only the Python standard library.

### Validation and evaluation

`scripts/validate_release.py` checks repository structure and required protocol coverage. Unit tests check that generated bundles contain expected files. The scenario suite evaluates model behavior manually or with a model-evaluation harness; repository tests do not claim to benchmark any model.

## Behavior model

The protocol follows a proportionality principle: choose the lowest level of rigor that responsibly handles the task. Deep analysis is not a virtue when it adds no decision value. Formal methods are selected by problem signal, not displayed as a fixed checklist.

## State and persistence

ØMEGA Modus is stateless by default. It can use only the current conversation, current files, host memory, and authorized tools. Persistent project history is not included in 1.0; claims of cross-session learning are prohibited unless the host provides it.
