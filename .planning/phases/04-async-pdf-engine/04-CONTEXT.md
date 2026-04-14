# Phase 4: Async PDF Engine - Context

**Gathered:** 2026-04-14
**Status:** Ready for planning

<domain>
## Phase Boundary
Enabling background processing for PDF generation. This phase implements the infrastructure for long-running tasks (Celery/Redis) and the high-fidelity rendering engine (WeasyPrint). The goal is to move PDF creation out of the request-response cycle.

</domain>

<decisions>
## Implementation Decisions

### Background Tasks (Celery & Redis)
- [LOCKED] Use **Redis** as the message broker and result backend.
- [LOCKED] Implement **Celery** for task management.
- [LOCKED] Define a `generate_pdf_task` that takes resume data and returns a file path or URL.

### PDF Engine (WeasyPrint)
- [LOCKED] Replace `xhtml2pdf` with **WeasyPrint** for better CSS support (Flexbox/Grid).
- [LOCKED] Use a dedicated `resume_print.html` template optimized for A4 paper.

### API Feedback Loop
- [LOCKED] Use a `TaskID` based polling system where the frontend checks `/api/v1/pdf/status/<task_id>/`.
- [LOCKED] Store generated PDFs in `media/resumes/` with a temporary lifecycle or unique hashing.

### Claude's Discretion
- Specific Celery worker configuration (serialization, concurrency).
- Media storage cleanup strategy (e.g., cron or simple file checking).

</decisions>

<canonical_refs>
## Canonical References
- `resume_project/celery.py` — New file to be created.
- `resume_app/tasks.py` — New file to be created.

</canonical_refs>

---
*Phase: 04-async-pdf-engine*
*Context gathered: 2026-04-14 via discussion*
