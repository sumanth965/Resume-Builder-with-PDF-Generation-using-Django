# Resume Builder Pro (Django Upgrade)

## What This Is

Resume Builder Pro is a modern web application designed to help users create, edit, and export professional resumes. It upgrades a basic legacy system into a scalable platform with real-time feedback and high-fidelity PDF output.

## Core Value

Empower users to create professional, high-quality resumes with a seamless, modern editing experience and reliable PDF generation.

## Requirements

### Validated

<!-- Shipped and confirmed valuable from legacy system -->

- ✓ Basic resume data persistence (Contact info, Education, Experience) — Legacy
- ✓ Form-based data entry — Legacy
- ✓ PDF export capability — Legacy

### Active

<!-- Current scope build toward -->

- [ ] **Modern UI Refresh**: Implement a response, premium design using Tailwind CSS.
- [ ] **Interactive Live Preview**: Real-time resume preview using Alpine.js and Django templates.
- [ ] **API Backbone (DRF)**: Implement Django REST Framework to enable scalable data handling and future integrations.
- [ ] **High-Fidelity PDF Generation**: Transition from `xhtml2pdf` to `WeasyPrint` or `Playwright` for modern CSS support and better layouts.
- [ ] **Database Refactor**: Re-structure the schema to support robust edit/update cycles and modular templates.
- [ ] **Template System**: Initial set of professional templates (Modern, Minimal, Professional) managed by developers.

### Out of Scope

<!-- Explicit boundaries to prevent scope creep -->

- **User-Level Design Customization**: Allowing users to change arbitrary colors/fonts is deferred to future milestones.
- **Full SPA Conversion**: Using React/Vue is excluded to keep the stack simple and maintainable within Django.
- **User Authentication**: Login/Accounts are not required for the initial upgrade version.

## Context

- **Legacy State**: Current system is a single-form monolithic Django app with inconsistent parsing logic and limited styling.
- **Tech Ecosystem**: Django 5.x environment on Python 3.14.
- **Feedback**: Need for more "premium" feel and reliable PDF layouts that match the screen UI.

## Constraints

- **Tech Stack**: Must remain within Django templates + Tailwind/Alpine.js stack.
- **Database**: Must use specialized migration paths if refactoring to ensure field consistency.
- **PDF Compatibility**: Must support modern CSS (Flexbox/Grid), which necessitates moving away from `xhtml2pdf`.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Hybrid Frontend | Use Tailwind/Alpine instead of React to reduce complexity while maintaining modern feel. | — Pending |
| Move to WeasyPrint | Need for Flexbox/Grid support in PDF generation that xhtml2pdf lacks. | — Pending |
| Schema Refactor | Explicit structure is needed for granular "Edit/Update" functionality. | — Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd-transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-04-14 after initialization*
