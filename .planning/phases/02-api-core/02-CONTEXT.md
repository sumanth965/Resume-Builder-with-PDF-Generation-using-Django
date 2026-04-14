# Phase 2: API Core (DRF) - Context

**Gathered:** 2026-04-14
**Status:** Ready for planning

<domain>
## Phase Boundary
Enabling programmatic access to the new relational schema by implementing a robust API layer using Django REST Framework. This serves as the bridge between the database and the future modern UI.

</domain>

<decisions>
## Implementation Decisions

### Framework & Structure
- [LOCKED] Use **Django REST Framework (DRF)**.
- [LOCKED] Implement **ModelViewSets** for Resume, Education, and Experience to ensure full CRUD capabilities.
- [LOCKED] Use **Nested Serializers** to return Education and Experience as part of the Resume object (GET /resumes/{id}/).

### Features
- [LOCKED] **Search/Filter**: Add `DjangoFilterBackend` and `SearchFilter` for `Resume` (search by name, skills).
- [LOCKED] **Validation**: Ensure DRF serializers enforce the same strict validation rules as the models.

### Claude's Discretion
- Choice of specific URL patterns (e.g., `/api/v1/resumes/`).
- Implementation of PDF generation endpoint (as placeholder or early version).

</decisions>

<canonical_refs>
## Canonical References
- `resume_app/models.py` — Source schema for serializers.
- `resume_project/urls.py` — Entry point for API routing.

</canonical_refs>

---
*Phase: 02-api-core*
*Context gathered: 2026-04-14 via discussion*
