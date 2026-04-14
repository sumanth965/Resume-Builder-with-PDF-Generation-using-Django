# Codebase Concerns

**Analysis Date:** 2026-04-14

## Tech Debt

**Monolithic View Logic:**
- Issue: `create_resume` view in `resume_app/views.py` handles parsing, database saving, context preparation, and PDF generation in a single large block.
- Why: Simple implementation for a single-app project.
- Impact: Hard to maintain, difficult to unit test individual parts of the logic.
- Fix approach: Refactor into separate service functions for parsing, data handling, and PDF rendering.

**Hardcoded Secrets:**
- Issue: `SECRET_KEY` is hardcoded in `resume_project/settings.py`.
- Why: Default Django setup.
- Impact: Security risk if the code is published to a repository.
- Fix approach: Move to environment variables using `python-dotenv`.

## Security Considerations

**Input Injection in PDF:**
- Risk: `xhtml2pdf` renders HTML directly. If user input (names, education) contains malicious HTML tags, it could lead to unexpected PDF rendering behavior or potential SSRF/XSS depending on the library's sandboxing.
- Current mitigation: None (Standard Django `request.POST.get`).
- Recommendations: Sanitize all user input before passing it to the PDF template using `bleach` or similar.

**Debug Mode Enabled:**
- Risk: `DEBUG = True` is set in `settings.py`.
- Current mitigation: None.
- Recommendations: Set `DEBUG = False` and configure `ALLOWED_HOSTS` for any non-local deployment.

## Performance Bottlenecks

**Synchronous PDF Rendering:**
- Problem: `pisa.CreatePDF` is a blocking operation.
- Measurement: Not measured, but typically takes 100-500ms depending on template complexity.
- Cause: Complex CSS parsing and PDF generation happen in the request-response thread.
- Improvement path: Move PDF generation to a background task (e.g., Celery) for large-scale use.

**SQLite for Scaling:**
- Problem: SQLite may hit locking issues under high concurrent write load.
- Cause: File-based locking mechanism of SQLite.
- Improvement path: Migrate to PostgreSQL for production environments.

## Fragile Areas

**Education Data Parsing:**
- Why fragile: The parsing logic in `resume_app/views.py` (lines 63-83) relies on hardcoded string prefixes (`College:`, `Course:`, `Marks:`).
- Common failures: If a user enters data without these exact prefixes or with extra spaces, the education history will be empty or malformed.
- Safe modification: Transition to a structured Formset or JSON-based input for education entries.

## Missing Critical Features

**User Authentication:**
- Problem: No login system. Any visitor can create resumes and save them to the global database.
- Current workaround: None.
- Blocks: Multi-user support, private resume storage.
- Implementation complexity: Medium (Use `django.contrib.auth`).

**Resume Management:**
- Problem: No list view or edit/delete functionality for existing resumes.
- Current workaround: Users must recreate the resume from scratch each time.
- Blocks: User retention and convenience.

---

*Concerns audit: 2026-04-14*
*Update as issues are fixed or new ones discovered*
