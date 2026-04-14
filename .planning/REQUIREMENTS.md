# Requirements: Resume Builder Pro (Django Upgrade)

**Defined:** 2026-04-14
**Core Value:** Empower users to create professional, high-quality resumes with a seamless, modern editing experience and reliable PDF generation.

## v1 Requirements

### Data & Storage (DATA)
- [ ] **DATA-01**: Refactor database schema to use structured models for Education and Experience (one-to-many relationships).
- [ ] **DATA-02**: Migrate existing SQLite data (if any) to the new structured schema.
- [ ] **DATA-03**: Support PostgreSQL as the production database engine.

### Backend & API (BACK)
- [ ] **BACK-01**: Implement Django REST Framework (DRF) for Resume, Education, and Experience models.
- [ ] **BACK-02**: Integrated WeasyPrint for modern CSS support in PDF generation.
- [ ] **BACK-03**: Configure Celery and Redis for asynchronous PDF generation tasks.
- [ ] **BACK-04**: Implement API endpoint for real-time PDF generation status.

### Frontend & UI (FRONT)
- [ ] **FRONT-01**: Set up Tailwind CSS for modern utility-first styling.
- [ ] **FRONT-02**: Implement a responsive sidebar-based layout (Editor on left, Preview on right).
- [ ] **FRONT-03**: Use Alpine.js for lightweight state management in the editor.
- [ ] **FRONT-04**: Use HTMX for partial page updates (e.g., adding/removing experience blocks).

### Resume Features (FEAT)
- [ ] **FEAT-01**: Implement "Modern" template using modern typography and clean spacing.
- [ ] **FEAT-02**: Implement "Professional" template using a traditional, compact layout.
- [ ] **FEAT-03**: Implement "Minimal" template using excessive whitespace and simple fonts.
- [ ] **FEAT-04**: Real-time "Live Preview" of the resume as the user types in the editor.
- [ ] **FEAT-05**: Ability to edit existing resume data with consistent save/update cycles.

## v2 Requirements (Deferred)
- **AUTH-01**: User accounts and secure private resume storage.
- **FEAT-06**: User-controllable color palettes and custom fonts.
- **FEAT-07**: Multi-resume management (manage different versions per user).
- **FEAT-08**: ATS Score feedback for content quality.

## Out of Scope
| Feature | Reason |
|---------|--------|
| React/Vue SPA | Keeping the stack simple and maintainable within Django templates. |
| AI Content Generation | Priority is on infrastructure and UI first. |
| Chrome Extension | Deferring until platform stability is reached. |

## Traceability
*To be populated during roadmap creation.*

| Requirement | Phase | Status |
|-------------|-------|--------|
| DATA-01 | — | Pending |
| DATA-02 | — | Pending |
| DATA-03 | — | Pending |
| BACK-01 | — | Pending |
| BACK-02 | — | Pending |
| BACK-03 | — | Pending |
| BACK-04 | — | Pending |
| FRONT-01 | — | Pending |
| FRONT-02 | — | Pending |
| FRONT-03 | — | Pending |
| FRONT-04 | — | Pending |
| FEAT-01 | — | Pending |
| FEAT-02 | — | Pending |
| FEAT-03 | — | Pending |
| FEAT-04 | — | Pending |
| FEAT-05 | — | Pending |

**Coverage:**
- v1 requirements: 16 total
- Mapped to phases: 0
- Unmapped: 16 ⚠️

---
*Requirements defined: 2026-04-14*
*Last updated: 2026-04-14 after initial definition*
