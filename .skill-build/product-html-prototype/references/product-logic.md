# Product Logic Checklist

Use this reference when the request is vague, combines too many ideas, or risks turning into a visual shell with no real workflow behind it.

## 1. Frame the job

- Who is the primary user?
- What event causes them to open this page?
- How often do they do this?
- What is at stake if they make the wrong choice or move too slowly?

## 2. Define the outcome

- What is the page trying to help the user accomplish?
- What should feel easier after this design exists?
- What business or operational outcome should the interface improve?

## 3. Identify the core objects

List the things the interface is about. Good prototypes usually revolve around a few explicit nouns:

- records
- assets
- alerts
- queues
- people
- approvals
- segments
- orders
- campaigns

If the nouns are unclear, the page structure will usually become vague too.

## 4. Sketch the primary flow

Most product pages should make this sequence legible:

1. orient
2. inspect
3. compare
4. decide
5. act
6. confirm

If a step is missing from the product story, the design should explain why.

## 5. Cover supporting states

Add only the states that matter, but do not ignore them:

- empty
- loading
- stale data
- partial success
- hard failure
- permission locked
- needs approval
- completed

## 6. Translate logic into sections

Useful section types:

- context strip: status, filters, scope, time range
- action surface: the place where a person makes the core move
- evidence panel: data, history, reasoning, risk, comparison
- system feedback: alerts, confirmations, blockers, recommendations
- next-step rail: what to do after the current decision

Each section should answer a question the user naturally has.

## 7. Sanity check before coding

- Can a reviewer explain the page purpose after a quick scan?
- Does the layout make the primary action obvious?
- Are the supporting metrics helping a decision, or just decorating the page?
- Would the design still make sense if all gradients were removed?
- Is there enough detail to feel like a product proposal instead of a wireframe?
