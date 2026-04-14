# Phase 5: Interactive Live Preview - Context

**Gathered:** 2026-04-14
**Status:** Ready for planning

<domain>
## Phase Boundary
Closing the loop between the editor and the preview pane. This phase ensures that all data (including dynamic relational blocks) is visible in real-time. The goal is a "What You See Is What You Get" (WYSIWYG) experience before the user hits "Download".

</domain>

<decisions>
## Implementation Decisions

### Preview Architecture
- [LOCKED] Use **HTMX Partial Swapping** for the preview pane.
- [LOCKED] Implement a `live_preview` view that returns an HTML fragment representing the current state of the resume.
- [LOCKED] High-performance debounce: Use `hx-trigger="keyup changed delay:800ms, change delay:800ms"`.

### UI Integration
- [LOCKED] Replace the "Placeholder" in the preview window with dynamic content.
- [LOCKED] Ensure the preview uses the same design tokens (Tailwind) as the main application but scoped to a "Document" container.

### Claude's Discretion
- Choice of whether to use Alpine.js for 100% instant sync of identity fields (hybrid approach) or move everything to HTMX. (Decision: Hybrid - identity is instant, sections are HTMX).

</decisions>

<canonical_refs>
## Canonical References
- `resume_app/templates/partials/preview_pane.html` — New file.

</canonical_refs>

---
*Phase: 05-interactive-live-preview*
*Context gathered: 2026-04-14 via discussion*
