# Security Policy

## Scope

ØMEGA Modus is an instruction framework, not an executable agent runtime or security product. Security issues may still arise from unsafe guidance, misleading approval rules, unsafe generated scripts, or accidentally included secrets.

## Reporting

Do not publish credentials, private data, or a weaponizable exploit in a public issue.

Report suspected issues privately through GitHub's private vulnerability reporting: open a security advisory on the **Security** tab of the repository and select **Report a vulnerability**. This channel is available only if the maintainer has enabled it under **Settings → Security → Private vulnerability reporting**.

If that form is not available, open a public issue titled `Security report` with a short, non-sensitive summary only, and ask for a private channel. Never include credentials, private data, or reproduction steps that could be weaponized.

## Maintainer response checklist

- Confirm the affected version and adapter.
- Determine whether the issue is an instruction defect, platform behavior, or user-environment problem.
- Add a regression scenario.
- Publish a patched release and changelog entry when appropriate.

## User safety

Do not treat prompt instructions as enforceable permissions. Configure platform permissions, sandboxing, secrets handling, and approval controls independently.
