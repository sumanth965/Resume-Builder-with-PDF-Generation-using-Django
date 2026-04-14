# Phase 2: API Core - Research

**Conducted:** 2026-04-14
**Status:** Complete

## DRF Best Practices for Nested Data (2024/2025)

### Writable Nested Serializers
- **Standard behavior**: Nested serializers are read-only by default.
- **Manual Implementation**: Required for `create()` and `update()` methods in the parent serializer to handle related `Education` and `Experience` records.
- **Tooling**: `drf-writable-nested` is a viable option for reducing boilerplate if complexity grows, but manual override is preferred for explicit control in the initial version.

### Performance Optimization
- **N+1 Avoidance**: Use `prefetch_related('education_entries', 'experience_entries')` in the `ResumeViewSet` to ensure efficient data fetching.
- **Payload Management**: Keep nesting levels shallow (limit to 1 level for this project).

### Search & Filtering
- **Django-filter**: Use `django-filter` package for robust query parameter support (e.g., `?name__icontains=`).
- **Standard Filters**: Implement `SearchFilter` for multi-field text search.

## Implementation Guardrails
- Ensure `HyperlinkedModelSerializer` is used if web navigation is desired, otherwise stick to `ModelSerializer` for client-side consumption simplicity.
- Add specific `v1/` prefixing in URL routing for future-proofing.
