# Codebase Structure

**Analysis Date:** 2026-04-14

## Directory Layout

```
resume_project/
├── .gemini/            # GSD system tools and commands
├── .planning/          # Project planning and memory
│   └── codebase/      # Current codebase map (this)
├── resume_project/     # Project configuration (Settings, WSGI/ASGI)
├── resume_app/         # Application source code
│   ├── migrations/    # Database schema history
│   ├── templates/     # HTML templates (Forms, PDF)
│   ├── views.py       # Request handlers
│   ├── models.py      # Database schema
│   └── urls.py        # App-specific routing
├── db.sqlite3          # Local database
├── manage.py           # Django management script
└── requirements.txt    # Project dependencies
```

## Directory Purposes

**resume_project/**
- Purpose: Global settings and deployment config.
- Contains: `settings.py`, `urls.py`, `wsgi.py`.
- Key files: `settings.py` - Single source of truth for config.

**resume_app/**
- Purpose: Application-specific logic.
- Contains: Views, Models, Forms, and Subdirectories for resources.
- Key files: `views.py` (PDF logic), `models.py` (Resume schema).

**resume_app/templates/**
- Purpose: Frontend and PDF presentation.
- Contains: `form.html` (input), `resume_template.html` (output layout).
- Key files: `resume_template.html` - CSS/HTML used by xhtml2pdf.

**.planning/**
- Purpose: GSD workflow state and project documentation.
- Contains: Codebase maps, project specs, roadmaps.

## Key File Locations

**Entry Points:**
- `manage.py`: Management CLI.
- `resume_project/urls.py`: Main URL entry point.

**Configuration:**
- `resume_project/settings.py`: Core Django settings.
- `requirements.txt`: Python dependencies.

**Core Logic:**
- `resume_app/views.py`: Main logic for data parsing and PDF generation.
- `resume_app/models.py`: Resume data structure.

## Naming Conventions

**Files:**
- lowercase_with_underscores.py: Standard Python naming for modules and functions.
- lowercase_with_underscores.html: Standard Django template naming.

**Directories:**
- lowercase_with_underscores: App and project directories.

## Where to Add New Code

**New Field to Resume:**
- Implementation: `resume_app/models.py`.
- UI: `resume_app/templates/form.html` and `resume_app/templates/resume_template.html`.
- Logic: `resume_app/views.py`.

**New PDF Template:**
- Implementation: `resume_app/templates/`.
- Logic: `resume_app/views.py` (referencing the new template name).

**New API Endpoint:**
- Definition: `resume_app/urls.py`.
- Handler: `resume_app/views.py`.

## Special Directories

**resume_app/migrations/**
- Purpose: Auto-generated DB migration files.
- Committed: Yes.

---

*Structure analysis: 2026-04-14*
*Update when directory structure changes*
