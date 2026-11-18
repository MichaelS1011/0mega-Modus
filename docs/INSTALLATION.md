# Installation Guide

## 1. Build adapter bundles

From the repository root:

```bash
python scripts/build_release.py
```

This creates `dist/omega-modus-v1.1.0/` without deleting unrelated files already present in `dist/`. Use the matching bundle under `dist/omega-modus-v1.1.0/bundles/`. ZIP archives for every adapter and the complete source tree are written to `dist/omega-modus-v1.1.0/archives/`. The instructions below describe the general installation approach; exact UI labels may differ by app version.

## 2. Choose one primary adapter

### OpenAI Codex

Use the `dist/omega-modus-v1.1.0/bundles/codex/` bundle.

- Copy `AGENTS.md` into the root of the target project, or merge its short guidance into an existing `AGENTS.md`.
- Copy `.agents/skills/omega-modus/` into the target project's `.agents/skills/` directory for project scope, or the supported user-level skill directory for user scope.
- Start a new Codex session. Invoke `$omega-modus` or describe a task that matches the skill.

Codex uses `AGENTS.md` for persistent project guidance and Agent Skills for reusable workflows. Check the current Codex documentation for supported scope and paths.

### Claude Code

Use the `dist/omega-modus-v1.1.0/bundles/claude-code/` bundle.

- Copy `.claude/skills/omega-modus/` into the target project's `.claude/skills/` directory for project scope, or your user-level Claude skills directory for personal scope.
- Start or refresh the Claude Code session.
- Invoke `/omega-modus` or let the skill description select it for a matching task.

Claude Code also supports `CLAUDE.md` project instructions. This release uses a skill-first adapter to keep the global instruction footprint small.

### Gemini CLI

Use the `dist/omega-modus-v1.1.0/bundles/gemini-cli/` bundle.

- Copy `GEMINI.md` into your project root, or merge its guidance into an existing file.
- For project scope, copy `.agents/skills/omega-modus/` into the target project's `.agents/skills/` directory. For user scope, copy it into `~/.agents/skills/` (or use the corresponding Gemini CLI skill-management command).
- Start a new session or refresh skills with `/skills reload`. Verify discovery with `/skills list`.

`GEMINI.md` provides persistent context. Agent Skills provide on-demand workflow instructions and may require an explicit consent prompt when activated.

### Cursor

Use the `dist/omega-modus-v1.1.0/bundles/cursor/` bundle.

- Copy `.cursor/rules/omega-modus.mdc` into the target project's `.cursor/rules/` directory.
- Open Cursor and confirm the rule is enabled in the Rules interface.
- If your project already has extensive rules, review for conflicts and avoid duplicate copies of the full protocol.

The `.mdc` file includes frontmatter and is configured as an always-applied project rule. Cursor also supports `AGENTS.md`; the `.mdc` path is used here for native rule control.

### GitHub Copilot

Use `dist/omega-modus-v1.1.0/bundles/github-copilot/`.

- Copy `.github/copilot-instructions.md` into the target project's `.github/` directory.
- Copy `.github/skills/omega-modus/` into the target project's `.github/skills/` directory where Agent Skills are supported.
- Review the file with any existing Copilot or agent instructions to avoid conflicts.
- Confirm repository custom instructions are enabled in the client or feature you use.

Support differs by Copilot client and feature. The adapter is a repository-wide instruction file, not a standalone extension.

### ChatGPT

Use `dist/omega-modus-v1.1.0/bundles/chatgpt/`.

- For a supported Skills-enabled ChatGPT desktop environment, install the included `SKILL.md` skill folder using that environment's skill workflow.
- For ChatGPT surfaces without skill installation, copy the contents of `instructions.md` into the relevant user/project instruction field or paste it at the start of a conversation.
- For Codex, prefer the dedicated Codex adapter rather than the generic ChatGPT instruction copy.

Availability of Skills and customization controls varies by ChatGPT product surface and plan. This adapter does not guarantee that every ChatGPT interface supports persistent global instructions.

### Generic AI assistant

Use `dist/omega-modus-v1.1.0/bundles/generic/OMEGA-MODUS-PROMPT.md`. Paste it into the assistant's system/project instruction field where available, or into a new conversation. The assistant must support custom instructions for persistence; otherwise it applies only to that conversation.

## 3. Avoid duplicate activation

Install one primary adapter per agent environment. Do not simultaneously add the Cursor rule, Copilot instructions, and multiple copies of the same core prompt to the same assistant context unless you intentionally want combined instructions. Duplicate instructions increase context use and may create conflicts.

## 4. Smoke test

Try the prompts in the main README. Confirm that QUICK tasks stay short and that complex tasks get cause analysis, risk controls, and honest verification.

## 5. Uninstall

Remove the ØMEGA Modus files you copied. If you merged content into existing instruction files, remove only the ØMEGA Modus section. Restart or reload the target environment.
