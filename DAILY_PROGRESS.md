# Daily Progress Log

Daily assignment tracking

## Date: 2026-04-22
### Goal for today
- Review the assignment brief and GitHub workflow expectations.
- Prepare the repository for project tracking before implementation starts.

### What I completed
- Read the SkillSwap assignment brief.
- Read the GitHub workflow guidelines.
- Confirmed the required architecture, workflow rules, and delivery expectations.
- Added the initial `README.md`.
- Added the initial `DAILY_PROGRESS.md`.

### Issues worked on
- None yet

### Branches / PRs updated
- No feature branches or PRs yet.

### Services touched
- None yet

### Endpoints completed
- None yet

### Gateway / auth / integration completed
- None yet

### Testing / CI completed
- None yet

### Blockers
None yet

### Next step
- Create the first set of GitHub issues.
- Start the first focused branch for repository and service scaffolding.

## Date: 2026-04-24

### Goal for today
- Prepare the next issue for project scaffolding.

### What I completed
- Created Issue #1 for repository documentation and progress tracking.
- Opened Draft PR #2 for the initial README and daily progress log work.

### Issues worked on
- #1 Set up repository documentation and progress tracking

### Branches / PRs updated
- Branch: `feature/repo-scaffold`
- Draft PR: #2

### Services touched
- None

### Endpoints completed
- None

### Gateway / auth / integration completed
- None

### Testing / CI completed
- None

### Blockers
- None

### Next step
- Create the Sprint 1 service foundations issue.
- Start a focused service foundations branch from `main`.

## Date: 2026-04-25

### Goal for today
- Begin Sprint 1 service foundation work.
- Set up the first usable FastAPI microservice structure.

### What I completed
- Created Issue #3 for FastAPI service foundations.
- Created branch `feature/service-foundations`.
- Opened Draft PR #4.
- Added folders for the three FastAPI services.
- Added health endpoints.
- Added Dockerfiles and requirements files for each service.
- Added Docker Compose with PostgreSQL, Nginx, and the three services.
- Added starter Nginx routing.
- Added database setup modules for each service.
- Added initial SQLAlchemy models.

### Issues worked on
- #3 Set up FastAPI service foundations

### Branches / PRs updated
- Branch: `feature/service-foundations`
- Draft PR: #4
- Commits:
  - `e120fd7 feat(scaffold): add service foundation skeleton`
  - `c3fca52 feat(db): add service database setup modules`
  - `eba7fec feat(models): add initial service data models`

### Services touched
- Identity & Profile Service
- Session Service
- Notification Service

### Endpoints completed
- `GET /health`

### Gateway / auth / integration completed
- Added starter Nginx routing.
- No auth or service-to-service integration yet.

### Testing / CI completed
- Confirmed Python files compile.
- Confirmed Docker Compose config is valid.

### Blockers
- Docker Compose startup has not been tested yet.

### Next step
- Add starter schemas and create/list endpoints.

## Date: 2026-04-26

### Goal for today
- Add starter schemas and endpoints for the services.

### What I completed
- Added Pydantic schemas for profiles, sessions, and notifications.
- Added basic create/list endpoints for profiles.
- Added basic create/list endpoints for sessions.
- Added basic create/list endpoints for notifications.
- Added notification lookup by profile ID.
- Wired the new routers into each FastAPI service.
- Added startup table creation for the current SQLAlchemy models.

### Issues worked on
- #3 Set up FastAPI service foundations

### Branches / PRs updated
- Branch: `feature/service-foundations`
- Draft PR: #4

### Services touched
- Identity & Profile Service
- Session Service
- Notification Service

### Endpoints completed
- `POST /api/v1/profiles`
- `GET /api/v1/profiles`
- `POST /api/v1/sessions`
- `GET /api/v1/sessions`
- `POST /api/v1/notifications`
- `GET /api/v1/notifications`
- `GET /api/v1/notifications/profile/{profile_id}`

### Gateway / auth / integration completed
- Updated Nginx routing for `/api/v1/auth`, `/api/v1/mfa`, `/api/v1/profiles`, `/api/v1/sessions`, and `/api/v1/notifications`.

### Testing / CI completed
- Confirmed Python files compile.
- Confirmed Docker Compose config is valid.

### Blockers
- Docker Compose startup still needs to be tested.

### Next step
- Run Docker Compose.
- Test service health endpoints through Nginx.
- Test the starter database-backed endpoints.
