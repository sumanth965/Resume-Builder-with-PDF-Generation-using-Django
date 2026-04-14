# Roadmap: Resume Builder Pro (Django Upgrade)

## Overview

A structured upgrade path from a monolithic legacy resume builder to a modern, scalable, and feature-rich platform. We will first re-establish the data foundation, then build out the API and UI layers, and finally implement high-performance PDF generation and multiple templates.

## Phases

- [x] **Phase 1: Foundation & Schema Refactor** - Establish structured relational data models.
- [x] **Phase 2: API Core (DRF)** - Build the backend endpoints for data management.
- [x] **Phase 3: Frontend Refresh (UI/UX)** - Implement Tailwind CSS and Alpine.js layout.
- [x] **Phase 4: Async PDF Engine** - Set up Celery/WeasyPrint for background processing.
- [x] **Phase 5: Interactive Live Preview** - Real-time feedback loop between editor and preview.
- [x] **Phase 6: Multi-Template System** - Implementation of professional resume themes.
- [x] **Phase 7: Production Readiness** - Testing, polish, and final refinements.

## Phase Details

### Phase 1: Foundation & Schema Refactor
**Goal**: Transition from flat fields to structured relational data.
**Depends on**: Nothing
**Requirements**: DATA-01, DATA-03
**Success Criteria**:
  1. `Resume`, `EducationBlock`, and `ExperienceBlock` models exist and relate correctly.
  2. Database can be migrated to PostgreSQL without schema loss.
  3. Legacy data is successfully moved to the new structure.
**Plans**: 2 plans

Plans:
- [x] 01-01: Create new structured models and relationships.
- [x] 01-02: Write and execute migration scripts for existing data.

### Phase 2: API Core (DRF)
**Goal**: Create a scalable backend interface.
**Depends on**: Phase 1
**Requirements**: BACK-01
**Success Criteria**:
  1. DRF serializers handle all Resume and Block models.
  2. CRUD endpoints are fully functional for resume sections.
**Plans**: 1 plan

Plans:
- [x] 02-01: API Core Implementation (DRF, Serializers, Routing).

### Phase 3: Frontend Refresh (UI/UX)
**Goal**: Modernize the user interface and editor experience.
**Depends on**: Phase 2
**Requirements**: FRONT-01, FRONT-02, FRONT-03
**Success Criteria**:
  1. Tailwind CSS is integrated and layout is responsive.
  2. Alpine.js manages form state in the editor without page reloads.
  3. UI feels "premium" and matches modern web standards.
**Plans**: 2 plans

Plans:
- [x] 03-01: Foundation & Design System (Tailwind, Base Layout).
- [x] 03-02: Modern Editor & Interactivity (HTMX, Alpine Sync).

### Phase 4: Async PDF Engine
**Goal**: High-fidelity, non-blocking PDF production.
**Depends on**: Phase 1
**Requirements**: BACK-02, BACK-03, BACK-04
**Success Criteria**:
  1. Celery/Redis workers can process tasks in the background.
  2. WeasyPrint renders complex CSS (Flexbox) correctly.
  3. API status endpoint returns the status of PDF generation.
**Plans**: 2 plans

Plans:
- [x] 04-01: Async Infrastructure (Celery/Redis).
- [x] 04-02: High-Fidelity Rendering (WeasyPrint).

### Phase 5: Interactive Live Preview
**Goal**: Seamless feedback as users edit data.
**Depends on**: Phase 3, Phase 4
**Requirements**: FEAT-04, FRONT-04
**Success Criteria**:
  1. Changes in editor fields trigger a partial update of the preview.
  2. HTMX handles adding/removing dynamic blocks smoothly.
**Plans**: 1 plan

Plans:
- [x] 05-01: Live Preview Integration (HTMX/Alpine).

### Phase 6: Multi-Template System
**Goal**: Variety of professional resume designs.
**Depends on**: Phase 5
**Requirements**: FEAT-01, FEAT-02, FEAT-03
**Success Criteria**:
  1. User can toggle between Modern, Professional, and Minimal themes.
  2. PDF output matches the selected theme perfectly.
**Plans**: 3 plans

Plans:
- [x] 06-01: Modern Template Implementation.
- [x] 06-02: Professional Template Implementation.
- [x] 06-03: Minimal Template Implementation.

### Phase 7: Production Readiness
**Goal**: Polish and bug fixing.
**Depends on**: Phase 6
**Requirements**: FEAT-05
**Success Criteria**:
  1. All v1 requirements are fully verified.
  2. No critical bugs in the editor or PDF rendering.
**Plans**: 1 plan

Plans:
- [ ] 07-01: Final UI polish and end-to-end testing.

## Progress

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Foundation | 2/2 | Complete | 2026-04-14 |
| 2. API Core | 1/1 | Complete | 2026-04-14 |
| 3. Frontend | 2/2 | Complete | 2026-04-14 |
| 4. PDF Engine | 2/2 | Complete | 2026-04-14 |
| 5. Preview | 1/1 | Complete | 2026-04-14 |
| 6. Themes | 3/3 | Complete | 2026-04-14 |
| 7. Polish | 3/3 | Complete | 2026-04-14 |

---
*Roadmap defined: 2026-04-14*
*Last updated: 2026-04-14 after initial definition*
