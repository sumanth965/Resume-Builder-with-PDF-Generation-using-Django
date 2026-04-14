# Phase 3: Frontend Refresh - Research

**Conducted:** 2026-04-14
**Status:** Complete

## Technical Patterns for 2025

### Interactive Formsets (Alpine + HTMX)
- **Primary Pattern**: "Partial Replacement". Use HTMX to fetch empty form templates and inject them into the DOM.
- **State Management**: Use Alpine.js for local UI toggles (e.g., "Add Section" visibility) and real-time input mirroring for the preview pane.
- **Django Integration**: Return `HTML partials` from Django views instead of full pages for dynamic additions/deletions.

### Tailwind Design System
- **Layout**: Sidebar (Fixed, 1/3 width) and Preview (Scrolling, 2/3 width).
- **Typography**: Professional sans-serif (e.g., Inter/Roboto) for UI, and template-specific serif/sans for the resume preview.
- **Glassmorphism**: Use for sidebar background to create a premium, layered feel.

### Live Preview Sync
- **Implementation**: Alpine.js `x-model` on inputs combined with a "Preview Component" that renders the mirrored data in real-time.
- **Synchronization**: For simple fields, mirror immediately. For complex relational blocks, use HTMX `hx-trigger="keyup changed delay:500ms"` to update the preview pane from the server.

## Implementation Guardrails
- Ensure CSRF tokens are handled in all HTMX requests.
- Use `hx-swap="outerHTML"` for row replacements.
- Keep standard Django templates for the base structure to ensure the app remains SEO friendly and accessible.
