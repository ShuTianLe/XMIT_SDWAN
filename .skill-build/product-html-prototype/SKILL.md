---
name: product-html-prototype
description: Create polished static HTML product prototypes from product briefs, redesign requests, PRDs, or feature ideas. Use when Codex should act like a product manager plus frontend designer to turn requirements into a visually strong prototype that explains feature hierarchy, interaction flow, information architecture, and UI states without building backend systems.
---

# Product HTML Prototype

Turn product requirements into stakeholder-ready static HTML prototypes that explain what the product should do before anyone commits to implementation details.

## Default Output

Create a prototype that opens locally without a build step and is easy to iterate on.

- Default to a single page prototype unless the brief clearly spans multiple roles or distinct flows.
- Use `index.html`, `styles.css`, and `app.js` when the idea benefits from a cleaner structure or light interaction.
- Use believable product copy and mock data instead of lorem ipsum.

## Workflow

### 1. Build the product frame

- Identify the target user, main scenario, primary success action, and operating constraints.
- Extract the core objects on screen: alerts, assets, orders, approvals, leads, devices, reports, and similar domain entities.
- Turn vague requests into explicit assumptions and keep moving unless a wrong assumption would change the whole product direction.
- Read `references/product-logic.md` when the brief is fuzzy, overloaded, or missing user-flow detail.

### 2. Decide what the prototype must prove

- Choose the one to three product decisions the page needs to make obvious: prioritize work, compare options, approve risk, recover from failure, onboard a new user, and similar.
- Make the page demonstrate the workflow instead of only describing it.
- Include the states reviewers will ask about: empty, loading, error, permission, confirmation, and success states when they matter.

### 3. Map the page structure

- Choose a single page by default.
- Use multiple HTML files only when the request explicitly calls for separate journeys or handoffs.
- Read `references/page-blueprint.md` to choose a layout pattern that matches the product shape.
- Read `references/style-prompt-pack.md` when the user wants stronger art direction, a less generic result, or explicit anti-AI visual constraints.

### 4. Build the prototype

- Prefer semantic HTML, portable CSS, and light JavaScript.
- Add JavaScript only for interactions that help the concept land: tab switches, filters, staged reveals, steppers, drawers, and state toggles.
- Use `scripts/scaffold_prototype.py` to copy the starter kit in `assets/prototype-starter/` before customizing it.
- Keep the code edit-friendly. Another Codex instance should be able to patch it quickly.
- Match the page language to the user's brief. If the request is in Chinese, visible UI copy should default to Chinese unless the product domain truly requires English terms.

### 5. Raise the design quality

- Pick a visual direction on purpose before writing the page. Name the direction explicitly in the response.
- Start the deliverable with two or three sentences that explain the chosen style direction and the main design decisions, then output the runnable code.
- Avoid generic white-card SaaS layouts, default centered heroes, and copy-pasted dashboard tropes.
- Avoid large-radius rectangles, pill-heavy chrome, and repeated rounded blocks as the default container language.
- Do not put explanatory meta copy in the page itself. Visible text should belong to the product, not explain the design process.
- Define CSS variables early for color, spacing, type, radius, and motion decisions.
- Use bold typography, non-default font choices, layered backgrounds, and one or two meaningful motion cues.
- Make desktop and mobile both work.
- Favor clarity over decoration. Every visual element should support the product story.

### 6. Verify the prototype

- A stakeholder should understand the user, workflow, main decisions, and key UI states in under two minutes.
- Remove backend talk unless the user explicitly asks for it.
- Ensure the prototype still communicates value when viewed as a static screenshot.

## Product Logic Rules

- Lead with the user task, not the component list.
- Show why each module exists and how information moves between them.
- Reflect hierarchy: what is urgent, what is secondary, what is reference material.
- Expose the moments where a person must decide, confirm, compare, or recover.
- If the product is operational, make status, risk, and next action obvious.
- If the product is consumer-facing, make motivation, trust, and progression obvious.

## Design Rules

- Start from a clear product narrative: context, action surface, feedback, resolution.
- Use realistic labels, KPIs, filters, alerts, tables, and timelines that match the domain.
- If the brief is Chinese, avoid mixing Chinese titles with decorative English side labels or meta captions.
- Prefer a few strong layout ideas over many weak sections.
- Keep the page visually rich enough for review meetings, but simple enough to edit quickly.
- Preserve an existing design system only when the request explicitly says to follow one.
- Treat the style prompt pack as a default constraint set unless the user gives a stronger brand or design system.

## Useful Resources

- `references/product-logic.md`: brief decomposition, user-flow framing, and feature validation checklist.
- `references/page-blueprint.md`: layout patterns, section choices, and state coverage guidance.
- `references/style-prompt-pack.md`: reusable Chinese prompt snippets for strong visual direction, anti-template constraints, and Ant Design-style backoffice pages.
- `scripts/scaffold_prototype.py`: copy the starter kit into a destination folder and stamp it with a project name.
- `assets/prototype-starter/`: polished baseline HTML, CSS, and JavaScript files to adapt.

## Example Requests

- "Use this PRD to make a polished HTML prototype for a warehouse dashboard."
- "Turn this feature brief into a static page that explains the onboarding flow."
- "Design a beautiful admin console prototype from these notes. No backend, just product logic and UI."
