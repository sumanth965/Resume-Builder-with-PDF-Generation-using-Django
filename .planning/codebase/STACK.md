# Technology Stack

**Analysis Date:** 2026-04-14

## Languages

**Primary:**
- Python 3.14.2 - All application logic and server-side processing.

**Secondary:**
- HTML/CSS - Frontend templates and PDF styling.
- JavaScript - Basic frontend interaction (implied by Django templates).

## Runtime

**Environment:**
- Python 3.14.2 (LTS) - Standard Python interpreter.
- Django Development Server - Local execution.

**Package Manager:**
- pip 25.3 - Dependency management.
- Requirements: `requirements.txt` present.

## Frameworks

**Core:**
- Django 5.0.6 - Web framework for routing, models, and templating.

**Testing:**
- Django Test Framework - (Built-in, standard `tests.py` present).

## Key Dependencies

**Critical:**
- `xhtml2pdf` >= 0.2.14 - Core library for generating PDF resumes from HTML templates.
- `django` >= 5.0.0 - Primary web framework.

**Infrastructure:**
- `sqlite3` - Standard Python library for database interaction.

## Configuration

**Environment:**
- `resume_project/settings.py` - Central Django configuration.
- `SECRET_KEY` - Defined in `settings.py`.

**Build:**
- No custom build step (Standard Django asset management).

## Platform Requirements

**Development:**
- Windows (Current OS) - Runs natively with Python and Django.
- Any platform supporting Python 3.x.

**Production:**
- Not currently configured for production (uses `DEBUG = True` and SQLite).

---

*Stack analysis: 2026-04-14*
*Update after major dependency changes*
