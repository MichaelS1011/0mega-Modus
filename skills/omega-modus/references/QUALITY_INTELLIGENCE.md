# Quality Intelligence — Method Router and Playbook

## Purpose

Quality Intelligence selects a small number of suitable problem-solving and improvement methods. It should improve the work without turning every interaction into a management workshop. Method selection is usually invisible to the user; the result, material evidence, and important limitations are not hidden.

The toolkit combines methods used in quality management and continuous improvement. Their histories and origins differ; do not describe every method as exclusively Japanese.

## Router: choose by problem signal

| Signal | Preferred method(s) | Expected output |
|---|---|---|
| A process or result needs controlled improvement | PDCA/PDSA | Baseline, change, check, decision to adapt or standardize |
| A specific failure has occurred and its cause is unclear | Five Whys | Evidence-backed causal chain or explicitly unresolved hypotheses |
| Several causal families may contribute | Ishikawa | Structured cause map, evidence gaps, investigation priorities |
| A human or process error could recur | Poka-Yoke | Prevention/detection control, validation, fallback |
| A proposed change has meaningful failure modes | FMEA | Prioritized failure modes, effects, controls, owners/actions |
| Enough categorized observations exist to prioritize | Pareto | Ranked categories with counts/impact and caveats |
| A complex problem needs a concise shared narrative | A3 | Current state, target, causes, countermeasures, plan, follow-up |
| Small incremental improvements can be tested | Kaizen | Small change, owner, measure, review point |
| Process variation or data structure matters | Basic QC tools | Appropriate map, check sheet, chart, or distribution summary |

Use the minimum sufficient set. Methods may be combined when they answer different questions, e.g. Five Whys + Poka-Yoke + PDCA for a repeated operational defect. Do not run all methods by default.

## 1. PDCA / PDSA — improvement loop

**Plan:** State the problem or opportunity, baseline, target, proposed change, expected result, measure, and risk.

**Do:** Test or implement the change at a scale proportionate to consequence. Prefer a pilot or reversible trial when possible.

**Check / Study:** Compare observed results with the baseline and target. Identify unintended effects and data limitations. Do not confuse a plausible story with measured improvement.

**Act:** If evidence supports the change, standardize it proportionately. If not, revise the hypothesis or countermeasure and run another bounded cycle. Stop when the acceptance criterion is met, the test is inconclusive, or more data is required.

Use PDCA for a real change or improvement cycle, not for a one-line answer. PDSA's Study step may be more appropriate when learning from an experiment is central.

## 2. Five Whys — causal investigation

1. Define the observable problem precisely: what happened, where, when, and how often.
2. Ask why the observed event occurred.
3. For each answer, ask what evidence supports it and whether it is itself a symptom.
4. Continue only while each link is plausible and investigable; five is a mnemonic, not a required count.
5. Branch when multiple causes are plausible. Stop when the cause is actionable and supported, or mark it as a hypothesis that needs evidence.
6. Check for system conditions such as unclear process, missing validation, incentives, workload, environment, or unavailable information.
7. Link the countermeasure to the supported cause and define a verification measure.

Do not blame an individual by default. Do not claim a root cause from a single unverified answer. Complex failures may require a causal tree, Ishikawa, fault analysis, or specialist investigation.

## 3. Ishikawa — cause-and-effect map

Use when multiple causal families may contribute. Start with a precise effect statement. Create relevant branches; common manufacturing categories include people, methods, machines, materials, measurement, and environment, but adapt categories for software, services, research, or personal workflows. Add candidate causes without presenting them as facts. Mark evidence status and rank what should be tested first. A fishbone diagram organizes hypotheses; it does not prove causality.

## 4. Poka-Yoke — mistake-proofing

Design a control that prevents an error or makes it immediately detectable. Examples include input validation, required-field checks, safe defaults, pre-flight checks, schema constraints, confirmation gates, duplicate detection, idempotency, previews, rollback paths, and guardrails at the point of action.

Prefer:
- prevention over downstream correction when practical;
- the smallest control that blocks the known failure;
- useful errors and recovery paths;
- reversible defaults and clear user consent;
- tests for both valid and invalid cases.

Avoid controls that create needless friction, silently discard user work, or create a false sense of safety.

## 5. FMEA — prospective risk analysis

For a meaningful proposed change or process, identify:
- failure mode: how it could fail;
- effect: what happens if it does;
- cause: why it might occur;
- existing controls: how it is currently prevented or detected;
- action: what would reduce likelihood or impact;
- owner or decision point, when known.

Use qualitative Low / Medium / High ratings for severity, likelihood, and detectability when evidence is sparse. Explain the basis. Do not calculate or imply precise Risk Priority Numbers from invented or incomparable data. A severe failure must not be dismissed merely because a heuristic score is low. Prioritize safety, legal, privacy, financial, data-loss, and irreversible risks.

## 6. Pareto — evidence-based prioritization

Use only when the user supplies or tools retrieve an adequate set of categorized observations. State the population, period, metric, and denominator. Rank categories by count, cost, impact, or another defined measure. A cumulative percentage may help identify concentration. Do not assume that exactly 80% of impact comes from 20% of causes; treat 80/20 as a heuristic, not a law. Pareto ranking is descriptive and does not prove causation.

## 7. A3 — concise problem-solving narrative

Use for complex or cross-functional problems where a shared written picture is valuable. Keep the A3 proportional to the problem. Suggested sections:
1. Background and context.
2. Current condition with evidence.
3. Problem statement and gap to target.
4. Cause analysis and evidence status.
5. Target condition.
6. Countermeasures linked to causes.
7. Implementation plan, responsibilities, and timing.
8. Follow-up measure and review date.

Do not fill sections with invented data. Mark unknown values and responsible owners as open items.

## 8. Kaizen — incremental improvement

Look for small changes that reduce avoidable effort, errors, delays, or variation. Define a baseline and a measurable outcome when possible. Include the people affected in decisions that change their workflow. Do not claim continuous learning across sessions unless an actual persistent record is available and authorized.

## 9. Basic quality tools

Select only when they fit available evidence:
- **Process map / flowchart:** sequence, handoffs, queues, loops, and rework.
- **Check sheet:** consistent collection of repeated observations.
- **Cause-and-effect diagram:** qualitative cause organization.
- **Pareto chart:** ranked frequency or impact categories.
- **Histogram:** distribution of numeric observations with adequate sample size.
- **Scatter plot:** association between paired numeric variables; not proof of causation.
- **Control chart / run chart:** time-ordered data; use sound methods and adequate observations before making claims about process stability.

Do not create statistical confidence, process-control limits, or sample-size claims without the necessary data and method.

## Disclosure policy

The method router does not need to announce every internal method. Present the actionable conclusion in natural language. Name a method when the user asks, when the method explains an important decision, when collaboration requires a shared vocabulary, or when an audit trail is useful. For high-impact work, provide a short audit summary with the method used, evidence considered, checks performed, and remaining uncertainty.

## Further references

- ASQ, PDCA cycle: https://asq.org/quality-resources/pdca-cycle
- ASQ, quality tools A to Z (including Five Whys, FMEA, mistake-proofing, Pareto, and A3): https://asq.org/quality-resources/quality-tools
- ASQ, seven basic quality tools: https://asq.org/quality-resources/seven-basic-quality-tools
