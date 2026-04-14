# Phase 4: Async PDF Engine - Research

**Conducted:** 2026-04-14
**Status:** Complete

## Implementation Details for Windows

### Celery & Redis
- **Windows Support**: Celery 4+ does not officially support Windows due to the lack of specialized fork support.
- **Workaround**: Use `--pool=solo` for local development.
- **Broker**: Use Redis. Recommendation: **Memurai** or Redis for Windows via WSL.

### WeasyPrint Setup
- **Dependencies**: Requires `Pango`, `Cairo`, and `GDK-PixBuf`.
- **Installation**: Use `msys2` or the `gtk-sharp` installer to get the DLLs on the system PATH.
- **Django Integration**: `django-weasyprint` provides a convenient `WeasyTemplateResponseMixin`.

## Architecture for Background PDF
1. **Request**: User clicks "Download PDF".
2. **Task**: View triggers `generate_pdf_task.delay(resume_id)`.
3. **Response**: View returns `task_id` and redirects to a "Preparing..." screen.
4. **Polling**: Frontend (HTMX) polls `/api/v1/pdf/status/<task_id>/`.
5. **Completion**: Once finished, the status endpoint returns the media URL for the PDF.
6. **Download**: UI shows "Download Ready" button.

## Dependency Updates
- `celery`
- `redis`
- `weasyprint`
- `django-weasyprint` (optional but helpful)
