# Phase 6: Multi-Template System - Context

**Gathered:** 2026-04-14
**Status:** Ready for planning

<domain>
## Phase Boundary
Expanding the visual variety of the resumes. This phase implements three distinct professional themes. The goal is to provide users with options that suit different industries (e.g., tech vs. legal vs. creative).

</domain>

<decisions>
## Implementation Decisions

### Theme Architecture
- [LOCKED] Use a `template_name` parameter in the request POST data.
- [LOCKED] Implement theme-specific partials: `themes/modern.html`, `themes/professional.html`, `themes/minimal.html`.
- [LOCKED] Both the Live Preview and the PDF Engine will use the same theme partials to maintain consistency.

### Template Specifications
- [LOCKED] **Modern**: Inter font, Slate/Blue colors, large header, grid layout for skills.
- [LOCKED] **Professional**: Times New Roman / Serif font, Black/Gray accents, compact line height, traditional centered layout.
- [LOCKED] **Minimal**: Roboto / Sans-serif light, No borders, excessive whitespace, left-aligned only.

### UI Integration
- [LOCKED] Add a "Theme" selector (Cards or Dropdown) in the editor's sidebar.
- [LOCKED] The theme change will trigger an HTMX refresh of the preview pane.

### Claude's Discretion
- Specific Tailwind colors/spacing for each theme.
- CSS-only vs. Fragment-based swapping (Decision: Fragment-based for flexibility).

</decisions>

<canonical_refs>
## Canonical References
- `resume_app/templates/themes/modern.html` — New directory/file.
- `resume_app/templates/themes/professional.html` — New file.
- `resume_app/templates/themes/minimal.html` — New file.

</canonical_refs>

---
*Phase: 06-multi-template-system*
*Context gathered: 2026-04-14 via discussion*
