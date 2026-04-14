# Phase 6: Multi-Template System - Research

**Conducted:** 2026-04-14
**Status:** Complete

## Theme Definitions

### 1. Modern (v1 Style)
- **Philosophy**: High-contrast, clean, and screen-optimized.
- **Typography**: `Inter` (Sans-serif).
- **Colors**: Primary: Slate-900, Accent: Blue-600.
- **Visuals**: Iconography allowed, subtle rounded borders.

### 2. Professional (Corporate)
- **Philosophy**: Traditional, trustworthy, for banking/legal/consulting.
- **Typography**: `Lora` (Serif) for headings, `EB Garamond` or `Lato` (Sans-serif) for body.
- **Colors**: Monochrome (Black/Gray).
- **Visuals**: Centered items, horizontal dividers (`<hr>`), no icons.

### 3. Minimal (Creative/Modern)
- **Philosophy**: "Less is more," focus on content and negative space.
- **Typography**: `Roboto Mono` or `Open Sans` Light.
- **Colors**: Gray-800 text on pure white.
- **Visuals**: Left-aligned, no borders, single column, large margins.

## Implementation Path
1. **Model Update**: Add `template_name` to `Resume` model (keep default 'modern').
2. **Fragment Pattern**: 
   - `templates/themes/modern.html`
   - `templates/themes/professional.html`
   - `templates/themes/minimal.html`
3. **Controller**: `live_preview` and `generate_pdf_task` will now take `template_name` and select the appropriate fragment to include.
