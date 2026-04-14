# External Integrations

**Analysis Date:** 2026-04-14

## APIs & External Services

**Resume PDF Generation:**
- xhtml2pdf - Local library used to convert HTML templates to PDF.
  - Integration method: Integrated via `xhtml2pdf.pisa` in `views.py`.
  - Auth: None required (local processing).

## Data Storage

**Databases:**
- SQLite - Local file-based database.
  - Connection: via `settings.py` (`db.sqlite3`).
  - Client: Django ORM.
  - Migrations: Managed via `python manage.py makemigrations` and `migrate`.

**File Storage:**
- Local File System - Used for template storage and static assets.
  - Locations: `resume_app/templates/`, `static/` (if present).

## Authentication & Identity

**Auth Provider:**
- Django Contrib Auth - Standard Django session-based authentication.
  - Integration: `django.contrib.auth` in `INSTALLED_APPS`.

## Monitoring & Observability

**Logs:**
- Standard Output - Django development server logs to console.

## CI/CD & Deployment

**Hosting:**
- Localhost - Project is currently set up for local development.

## Environment Configuration

**Development:**
- Required env vars: None (all configured in `settings.py`).
- Secrets location: `SECRET_KEY` is hardcoded in `settings.py` (Security Risk for production).

---

*Integration audit: 2026-04-14*
*Update when adding/removing external services*
