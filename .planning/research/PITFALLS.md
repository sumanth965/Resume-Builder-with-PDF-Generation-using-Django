# Pitfalls Research: Django PDF & Data Generation

## Common Mistakes
1. **N+1 Logic in Templates**: Querying individual sub-records (e.g., specific education details) inside a loop in the PDF template, leading to massive DB overhead.
2. **Blocking PDF Generation**: Generating a PDF inside a standard View function. On slow machines or complex designs, this triggers gateway timeouts and poor UX.
3. **Fragile Input Parsing**: Relying on string-matching (like "College:") for multi-line text instead of structured relational data.
4. **CSS Layout Mismatch**: Expecting high-level modern CSS (Grid/Flex) to work in older PDF engines like `xhtml2pdf`.

## Prevention Strategies
- **Eager Loading**: Use `select_related()` and `prefetch_related()` when fetching resume data for rendering.
- **Background Tasks**: Always use Celery for any task taking longer than 200ms (like PDF generation).
- **Structured Fields**: Use Django's `JSONField` or a Related Model for education/experience instead of a single `TextField`.
- **Modern Engines**: Use `WeasyPrint` or `Playwright` to match modern UI design capabilities.

---
*Research Date: 2026-04-14*
