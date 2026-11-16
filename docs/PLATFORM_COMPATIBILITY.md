# Platform Compatibility

**Documentation review dates: 2026-11-15 and 2026-11-16.** Vendor features and paths can change. Re-check official documentation before publishing a new adapter revision.

| Platform | Adapter mechanism in this release | Notes |
|---|---|---|
| OpenAI Codex | `AGENTS.md` + Agent Skill under `.agents/skills/omega-modus/` | Codex supports project guidance and reusable skills. |
| Claude Code | Agent Skill under `.claude/skills/omega-modus/` | Skill is discoverable/invocable as `/omega-modus`; project-level instructions may also use `CLAUDE.md`. |
| Gemini CLI | `GEMINI.md` + Agent Skill under `.agents/skills/omega-modus/` | Workspace discovery supports `.agents/skills/`; user-level discovery supports `~/.agents/skills/`. Skill activation may request consent. |
| Cursor | `.cursor/rules/omega-modus.mdc` | Project rules require `.mdc` plus frontmatter; Cursor also supports `AGENTS.md`. |
| GitHub Copilot | `.github/copilot-instructions.md` + `.github/skills/omega-modus/` | Repository-wide custom instructions and Agent Skills on supported Copilot clients/features. |
| ChatGPT | Skill package where Skills are supported; otherwise copyable instructions | Not every ChatGPT surface supports installing or persistently applying a local skill. |
| Generic | Copy/paste prompt | Persistence depends on the target product's custom-instruction capability. |

## Verification status of the paths above

- **Checked against official documentation on 2026-11-16:** Claude Code project skills at `.claude/skills/<skill-name>/SKILL.md`; Gemini CLI workspace skills at `.gemini/skills/` or the `.agents/skills/` alias, and user-level skills at `~/.gemini/skills/` or `~/.agents/skills/`; Cursor project rules as `.mdc` files in `.cursor/rules` with frontmatter (`alwaysApply: false` plus a `description` for agent-selected inclusion; plain `.md` files there are ignored) and `AGENTS.md` as an alternative; GitHub Copilot repository-wide instructions at `.github/copilot-instructions.md` and project skills at `.github/skills/`, `.claude/skills/`, or `.agents/skills/`.
- **Partially checked:** Codex `AGENTS.md` is documented and is the primary carrier of the Codex adapter, so the adapter also works without the skill directory. The project-local `.agents/skills/` discovery path is consistent with the Agent Skills standard and current Codex skills documentation, but was not confirmed line by line.
- **Not checked:** ChatGPT support for installing a local skill package or persistently applying copied instructions varies by surface, plan, and account. The adapter therefore offers copyable instructions and claims no persistence.

## Official documentation

- OpenAI — Build skills: https://learn.chatgpt.com/docs/build-skills
- OpenAI — Codex customization overview: https://learn.chatgpt.com/docs/customization/overview
- OpenAI — Skills in plugins: https://developers.openai.com/plugins/concepts/skills
- Anthropic — Claude Code skills: https://code.claude.com/docs/en/skills
- Anthropic — Claude Code settings and instructions: https://code.claude.com/docs/en/settings
- Google — Gemini CLI Agent Skills: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md
- Google — Gemini CLI `GEMINI.md`: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md
- Cursor — Rules: https://cursor.com/docs/rules
- GitHub — Agent Skills: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills
- GitHub — Repository custom instructions: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions
- Agent Skills standard: https://agentskills.io/

## Compatibility philosophy

Adapters should describe only what the platform currently supports. Do not infer that a file being present guarantees the client loads it. Use the platform UI or documented context-inspection command to confirm activation where available. Keep the canonical protocol platform-neutral and make adapter changes independently.
