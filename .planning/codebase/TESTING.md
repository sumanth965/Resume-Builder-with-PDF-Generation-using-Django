# Testing Patterns

**Analysis Date:** 2026-04-14

## Test Framework

**Runner:**
- Django Test Runner (`django.test.TestCase`).

**Assertion Library:**
- Built-in Python `unittest` assertions.

**Run Commands:**
```bash
python manage.py test                 # Run all tests
python manage.py test resume_app      # Run app-specific tests
```

## Test File Organization

**Location:**
- `resume_app/tests.py`: Standard location for Django app tests.

**Naming:**
- `tests.py` for unit and integration tests.

## Test Structure

**Suite Organization:**
```python
from django.test import TestCase
from .models import Resume

class ResumeModelTest(TestCase):
    def test_resume_creation(self):
        # arrange
        # act
        # assert
        pass
```

## Mocking

**Framework:**
- `unittest.mock` (Standard Python library).

**What to Mock:**
- PDF generation calls (if needed to speed up tests).
- External integrations (if any were present).

## Fixtures and Factories

**Test Data:**
- Django `TestCase` handled DB isolation.
- Data typically created in `setUp` method or directly in test cases.

## Coverage

**Requirements:**
- No target currently defined.

**View Coverage:**
```bash
# Recommended tool: coverage.py
coverage run manage.py test
coverage report
```

## Test Types

**Unit Tests:**
- Test model logic and helper functions (e.g., `split_data`).

**Integration Tests:**
- Test View responses (200 OK, PDF content type).

---

*Testing analysis: 2026-04-14*
*Update when test patterns change*
