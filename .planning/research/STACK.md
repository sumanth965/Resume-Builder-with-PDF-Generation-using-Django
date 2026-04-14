# Stack Research: Resume Builder Pro (2026)

## Recommended Stack

**Backend:**
- **Django 5.x**: Core framework.
- **Django REST Framework (DRF)**: For API endpoints.
- **Django Environ**: For secure environment variable management.

**Frontend:**
- **Tailwind CSS**: Modern utility-first styling.
- **Alpine.js**: Lightweight interactivity for live previews and UI toggles.
- **HTMX**: For seamless partial page updates without full SPA complexity.

**Data & Tasks:**
- **PostgreSQL**: Standard reliable relational database.
- **Redis**: Message broker for task queues.
- **Celery**: Asynchronous PDF generation tasks.

**PDF Generation (Choice: WeasyPrint vs Playwright):**
- **Primary Choice: WeasyPrint**: Pure Python, easier deployment, excellent Paged Media CSS support.
- **Alternative: Playwright**: Use if templates require advanced JS execution or complex modern CSS that WeasyPrint might struggle with.

## Rationale
- **HTMX/Alpine.js**: Provides SPA-like interactivity while keeping logic in Django templates, matching the user's preference for avoiding React/Vue.
- **Celery/Redis**: Critical for UX; PDF generation is CPU-intensive and should never block the main web thread.
- **PostgreSQL**: Essential for the "scalable" requirement over the current SQLite.

---
*Research Date: 2026-04-14*
