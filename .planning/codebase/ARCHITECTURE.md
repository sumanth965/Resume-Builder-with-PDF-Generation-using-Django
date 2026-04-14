# Architecture

**Analysis Date:** 2026-04-14

## Pattern Overview

**Overall:** Full-stack MVC (Django)

**Key Characteristics:**
- Monolithic structure
- Model-Template-View (MTV) pattern
- Server-side PDF generation
- Synchronous request-response cycle

## Layers

**Presentation Layer:**
- Purpose: Render input forms and PDF structures
- Contains: Django Templates, CSS
- Location: `resume_app/templates/`
- Depends on: Context data from the View layer
- Used by: Users via browser

**Logic Layer (Views):**
- Purpose: Handle requests, parse form data, and orchestrate PDF creation
- Contains: `create_resume` view logic
- Location: `resume_app/views.py`
- Depends on: Model layer (storage), `xhtml2pdf` (generation)
- Used by: URL router

**Data Layer (Models):**
- Purpose: Persist resume data to the database
- Contains: `Resume` model definition
- Location: `resume_app/models.py`
- Depends on: Django ORM
- Used by: View layer

## Data Flow

**Resume Creation & PDF Generation:**

1. User accesses `/` and fills out `form.html`.
2. POST request is sent to `create_resume` view.
3. View extracts form fields (Contact, Education, Experience, etc.).
4. Data is saved as a new `Resume` instance in `db.sqlite3`.
5. View parses complex fields (e.g., Education lines) into context dictionaries.
6. Context is passed to `resume_template.html`.
7. `xhtml2pdf` (pisa) renders the HTML + Context into an `application/pdf` response.
8. PDF is downloaded by the user's browser.

**State Management:**
- Persistent: Resume data is stored in SQLite.
- Ephemeral: Session and form data handled by Django.

## Key Abstractions

**Resume Model:**
- Purpose: Represents a complete user resume record
- Location: `resume_app/models.py`
- Pattern: Django Model

**PDF Generator:**
- Purpose: Convert HTML to PDF stream
- Location: `resume_app/views.py` (inline using `xhtml2pdf`)
- Pattern: Library-based transformation

## Entry Points

**Django Entry:**
- Location: `manage.py`
- Triggers: CLI commands (runserver, migrate, etc.)
- Responsibilities: Server lifecycle and administrative tasks.

**Global URL Router:**
- Location: `resume_project/urls.py`
- Triggers: Incoming HTTP requests
- Responsibilities: Route requests to app-level URLs.

**App URL Router:**
- Location: `resume_app/urls.py`
- Triggers: Requests starting with `/`
- Responsibilities: Route to `views.create_resume`.

## Error Handling

**Strategy:** Default Django exception handling (500 error on crash, validation errors implied).

**Patterns:**
- Try/Except block for PDF generation (optional but recommended in future).
- Form data scrubbing in View layer (helper functions in `views.py`).

---

*Architecture analysis: 2026-04-14*
*Update when major patterns change*
