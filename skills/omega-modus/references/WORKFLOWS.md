# Workflow Patterns

These patterns show how the seven functions and Quality Intelligence work together. They are not mandatory templates; adapt them to the user's task.

## A. Research and factual analysis

1. SCAN: define question, scope, and required recency.
2. VERIFY: identify primary sources, compare dates, separate evidence from inference.
3. THINK: compare interpretations only when evidence supports more than one.
4. STRATEGIZE: define what would count as an adequate answer.
5. EXECUTE: browse or inspect only when tools are available and useful.
6. VALIDATE: check key claims, source dates, and contradictions.
7. REPORT: answer first, cite claims, explain limitations.

## B. Software development

1. SCAN: inspect project conventions, acceptance criteria, dependencies, and constraints.
2. VERIFY: inspect relevant files and current tests before editing.
3. THINK: consider minimal change versus larger redesign when materially different.
4. STRATEGIZE: identify the highest-risk regression and test plan.
5. EXECUTE: make focused changes; preserve unrelated code; seek approval for destructive or external changes.
6. VALIDATE: run relevant tests, lint, type checks, build, or manual checks that are available.
7. REPORT: summarize changed files, checks actually run, failures, and remaining risks.

Quality methods: use Five Whys/Ishikawa for recurring defects, Poka-Yoke for recurrence prevention, FMEA for risky changes, PDCA for validating improvement.

## C. Repeated operational problem

1. Define the observable problem and baseline.
2. Use Five Whys for a simple causal chain; Ishikawa when several cause families are plausible.
3. Verify the most important hypotheses with available data.
4. Use Pareto only if enough categorized observations exist.
5. Choose a countermeasure that addresses a supported cause.
6. Add a Poka-Yoke control where it can prevent or detect recurrence.
7. Use PDCA to compare results with the baseline and target.
8. Report what changed, what improved, and what remains uncertain.

## D. Complex initiative / A3

Create a concise A3 narrative with background, current condition, problem, target, cause evidence, countermeasures, implementation plan, owner, measures, and follow-up. Use FMEA for consequential failure modes. Obtain approvals at meaningful decision gates, not after every harmless action.

## E. Writing and content creation

Clarify audience, purpose, facts, format, and tone. Separate user-provided facts from proposed wording. For public claims, check sources when available. Use a content review checklist rather than forcing formal quality methods on every draft.

## F. Personal planning and everyday tasks

Keep the workflow lightweight. Help the user make progress, state material assumptions, and avoid unnecessary project-management overhead. Use a status report only when work spans multiple turns or has explicit milestones.
