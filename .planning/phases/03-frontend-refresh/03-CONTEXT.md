# Phase 3: Frontend Refresh (UI/UX) - Context

**Gathered:** 2026-04-14
**Status:** Ready for planning

<domain>
## Phase Boundary
Transforming the existing monolithic Django templates into a modern, responsive, and interactive user interface. This phase focuses on styling (Tailwind CSS) and lightweight interactivity (Alpine.js/HTMX) while maintaining the Django template architecture.

</domain>

<decisions>
## Implementation Decisions

### Styling (Tailwind CSS)
- [LOCKED] Use **Tailwind CSS** (via CDN for local dev parity or CLI for production optimization).
- [LOCKED] Implement a **Two-Pane Layout**: Sticky Sidebar Editor (left) and Live Preview (right).

### Interactivity
- [LOCKED] Use **Alpine.js** to manage the visibility of form sections and basic UI state (e.g., active tabs).
- [LOCKED] Use **HTMX** for dynamic list management (adding/removing Education or Experience blocks) without full page reloads.

### Template Architecture
- [LOCKED] Upgrade `base.html` to include the modern design system tokens (colors, typography).
- [LOCKED] Refactor `create_resume.html` into modular components (e.g., `_education_form.html`).

### Claude's Discretion
- Choice of specific Tailwind color palette (e.g., Slate/Blue for a professional look).
- Specific Alpine.js data structures for form state.

</decisions>

<canonical_refs>
## Canonical References
- `resume_app/templates/` — Existing templates to be refactored.
- `resume_app/static/` — Assets directory.

</canonical_refs>

---
*Phase: 03-frontend-refresh*
*Context gathered: 2026-04-14 via discussion*
