# Phase 1: Foundation & Schema Refactor - Context

**Gathered:** 2026-04-14
**Status:** Ready for planning

<domain>
## Phase Boundary
Upgrading the legacy monolithic resume data structure into a modular, relational schema while ensuring data safety and future PostgreSQL compatibility.

</domain>

<decisions>
## Implementation Decisions

### Database & Environment
- [LOCKED] Use **SQLite** for current development.
- [LOCKED] Implement **environment variables** (via `django-environ` or `python-dotenv`) for database configuration to allow zero-code switching to **PostgreSQL** in production.

### Schema Design
- [LOCKED] Implement **Related Models** for Education and Experience using `ForeignKey` relationships to the `Resume` model.
- [LOCKED] Maintain **legacy fields** in the `Resume` model as backups during this phase.

### Validation Rules
- [LOCKED] **Dates**: Must follow `YYYY-MM-DD` format.
- [LOCKED] **Mandatory Fields**: `name` and `email` on Resume; `degree`, `institution` on Education; `company`, `role` on Experience.
- [LOCKED] **Cardinality**: At least one education OR one experience entry is required for a valid resume.
- [LOCKED] **Formats**: Strict email validation and basic phone number formatting.

### Claude's Discretion
- Implementation of helper methods for data cleaning.
- Specific related_name choices (e.g., `resume.education_entries`).

</decisions>

<canonical_refs>
## Canonical References
- `resume_app/models.py` — Current flat models.
- `resume_app/views.py` — Existing parsing logic to be replicated/improved.

</canonical_refs>

---
*Phase: 01-foundation-refactor*
*Context gathered: 2026-04-14 via discussion*
