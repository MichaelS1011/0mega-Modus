# Changelog

All notable changes to ØMEGA Modus are documented here.

## [Unreleased]

### Changed
- README: added a plain-language "What you get" section stating the user-facing behaviours the protocol rules guarantee, with an explicit statement that the framework does not promise being faster or cheaper; the launch clip is linked as a file link because image embeds of MP4 files do not render on GitHub.

## [1.1.0] — 2026-11-17

### Changed
- Release version has a single source: `pyproject.toml`. Build and validation scripts derive it from there, and a tag gate fails the build when the built commit is tagged with a different version.
- Evaluation record template now covers S13–S15, and a test keeps the template rows in sync with the scenario files.
- README: 36-second launch clip (`assets/clip-terminal-proof.mp4`) embedded after “How it works”, and a “What it costs” section stating protocol sizes and the one paired run’s lengths, labeled as a preliminary single-run observation.
- Operating contract rule 6 now requires applying clearly safe, reversible fixes that are encountered while executing, verifying them, and reporting them as separate items; riskier findings stay recommendations. In A/B demo runs on 2026-11-16 (single run per condition) this was the only observed behavioral difference; full benchmark pending.
- Method routing is now a fixed protocol rule, not only a reference pointer: planning, option decisions, prioritization, and requirements have explicit routing rules, and failure investigation requires reproducing the problem, labeling causal hypotheses (assumed, supported, verified, open), and separating immediate relief, cause correction, and system improvement.
- Planning rules now require checking reuse (library, existing feature, off-the-shelf) before proposing to build, including or explicitly ruling out deferring/doing nothing with a one-line reason, and commitments as range estimates with a stated basis; in the 2026-11-16/17 planning A/B runs (single run per condition) both conditions silently skipped the reuse and do-nothing options, and the first protocol-guided run estimated without a basis.
- Updated S04 expected markers to include hypothesis labels and layered countermeasures; updated S15 markers to include the reuse/do-nothing check and range estimates.

### Added
- Tests: single-source version declaration, self-contained ChatGPT instructions, generic prompt reference coverage, and template/scenario consistency.
- `docs/PLATFORM_COMPATIBILITY.md`: manual activation checklist for the copy/paste adapters, with the surfaces explicitly marked as not hand-verified until the checklist is run per product surface.
- Evaluation scenario S13 (incidental safe fix), S14 (unverified green claim at a release gate), and S15 (planning and option decision).
- Quality Intelligence router rows and playbooks for work breakdown with a first verifiable increment, decision matrix, impact/effort and Pareto prioritization, assumptions with acceptance criteria, reuse check before build, range estimates, and result-first briefings.

## [1.0.0] — 2026-11-15

### Added
- Complete seven-function ØMEGA Modus operating protocol.
- Adaptive QUICK, STANDARD, and DEEP task-routing model.
- Quality Intelligence method router with PDCA/PDSA, Five Whys, Ishikawa, Poka-Yoke, FMEA, Pareto, A3, Kaizen, and basic QC tools.
- Evidence, uncertainty, execution, verification, safety, and human-approval rules.
- Native adapter bundles for Codex, Claude Code, Gemini CLI, Cursor, GitHub Copilot, ChatGPT-compatible instructions, and generic assistants.
- Twelve evaluation scenarios and a scoring rubric.
- Repository validation, release bundling, CI workflow, contribution guidance, and Apache-2.0 license.

### Notes
- The project was renamed from **OMEGA-7** to **ØMEGA Modus** before its first publication. The rename covers the repository name, skill name, adapter paths, bundle names, and documentation; the protocol content itself is unchanged.
- Version 1.0.0 is a complete instruction-framework release, not a guarantee of model behavior or a hosted software service.
- Adapter compatibility is based on official vendor documentation reviewed on 2026-11-15 and again on 2026-11-16. Per-platform verification status is recorded in `docs/PLATFORM_COMPATIBILITY.md`; vendor features and paths may change as platforms evolve.
