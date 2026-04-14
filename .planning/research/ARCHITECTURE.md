# Architecture Research: Scalable Resume Infrastructure

## System Overview
A modern Django architecture utilizing an API-first approach for critical interactive components while retaining server-side rendering for primary navigation.

## Component Boundaries
1. **Django App**: Handles routing, auth (future), and basic template rendering.
2. **DRF API**: Provides endpoints for resume data serialization and background task status.
3. **Task Queue (Celery)**: Offloads the intensive PDF generation process.
4. **Data Store**: PostgeSQL for structured resume objects, education blocks, and work history.

## Data Flow (Optimized)
1. **Edit**: User types in Alpine.js-powered form.
2. **Preview**: Alpine.js updates a local state for near-instant visual feedback.
3. **Auto-save (Future)**: Form data is pushed to DRF endpoints in the background.
4. **Generate**: User clicks "Download". Django triggers a Celery task.
5. **Download**: Client polls DRF for the finished PDF file path or receives a WebSocket notification.

## Build Order
1. **Schema Refactor**: Transition to structured models (Resume, EducationBlock, ExperienceBlock).
2. **API/Core**: Implement DRF endpoints for the new models.
3. **UI Refresh**: Integrate Tailwind/Alpine into Django templates.
4. **PDF Engine**: Implement the new WeasyPrint/Playwright backend.

---
*Research Date: 2026-04-14*
