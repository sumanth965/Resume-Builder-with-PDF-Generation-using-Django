# Phase 5: Interactive Live Preview - Research

**Conducted:** 2026-04-14
**Status:** Complete

## Strategic Patterns

### HTMX debounced Preview
- **Trigger**: `hx-trigger="keyup changed delay:1s, change"` on the main form.
- **Target**: `#preview-window`.
- **Logic**: The server-side `live_preview` view will perform the same data parsing as the `create_resume` view and render a specialized `preview_pane.html` partial.

### Hybrid Sync (Identity + Sections)
- **Identity Fields**: Use Alpine.js `x-model` for 0ms lag on Name, Email, Phone, and Objective.
- **Dynamic Sections**: Use HTMX for Education and Experience blocks. This avoids writing complex "Dynamic Alpine" logic to manage row indices in the frontend.

### Optimizations
- **Partial Template**: `preview_pane.html` will contain only the interior of the resume document.
- **Indicator**: Use a subtle "Syncing..." status indicator in the editor header while HTMX requests are in flight.
- **CSRF**: Handled globally in `base.html` using `htmx:configRequest`.
