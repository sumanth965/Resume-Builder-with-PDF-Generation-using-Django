# Coding Conventions

**Analysis Date:** 2026-04-14

## Naming Patterns

**Files:**
- lowercase_with_underscores.py (e.g., `views.py`, `models.py`)
- lowercase_with_underscores.html (e.g., `resume_template.html`)
- Standard Django filenames for app components.

**Functions:**
- snake_case for all functions (e.g., `create_resume`, `split_data`).

**Variables:**
- snake_case for local variables and model fields.
- UPPER_SNAKE_CASE for constant-like settings in `settings.py`.

**Classes:**
- PascalCase for Model and Form classes (e.g., `Resume`).

## Code Style

**Formatting:**
- Standard Python (PEP 8) style is evident.
- Indentation: 4 spaces.
- Blank lines: 2 between top-level definitions, 1 between methods.

**Linting:**
- Not currently configured with a specific tool in the repo.

## Import Organization

**Order:**
1. Standard library imports (`import os`, `from pathlib import Path`)
2. Django core imports (`from django.shortcuts import render`)
3. Third-party library imports (`from xhtml2pdf import pisa`)
4. Local application imports (`from .models import Resume`)

**Grouping:**
- Blank line between standard, third-party, and local groups.

## Error Handling

**Patterns:**
- Implicit handling via Django's default behavior.
- Manual sanitization of input data using helper functions (e.g., `split_data`, `split_lines` in `views.py`).

## Logging

**Framework:**
- Standard Python `logging` or Django defaults.
- Currently relies on `print()` or dev server logs for debugging.

## Comments

**When to Comment:**
- Structural markers: `# ---------- HELPERS ----------`, `# ---------- GET DATA ----------`.
- Important notes: `# ✅ IMPORTANT`, `# 🔥 ✅ SAVE TO DATABASE (ADDED HERE)`.
- Explaining logic: `# ---------- PDF ----------`.

## Function Design

**Size:**
- `create_resume` is currently quite large (~120 lines) as it contains multiple nested helper functions. Extraction of helpers is recommended for future growth.

**Parameters:**
- Standard Django view parameters: `request`.

---

*Convention analysis: 2026-04-14*
*Update when patterns change*
