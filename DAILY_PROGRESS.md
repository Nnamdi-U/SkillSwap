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
- Ran the full Docker Compose stack locally.
- Added a PostgreSQL healthcheck to `docker-compose.yml`.
- Updated service dependencies so FastAPI services wait for PostgreSQL to be healthy.
- Confirmed all containers start successfully.
- Tested health endpoints through Nginx.
- Tested starter database-backed endpoints through Nginx.
- Added `.dockerignore` files for each service.
- Removed the tracked `.DS_Store` file.

### Issues worked on
- #3 Set up FastAPI service foundations

### Branches / PRs updated
- Branch: `feature/service-foundations`
- Draft PR: #4
- Commit: `227192e feat(api): add starter service endpoints`
- Commit: `b7111b7 fix(compose): wait for postgres health before services`
- Commit: `4aca1e1 chore(repo): clean service build contexts`

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
- Confirmed `docker compose up --build -d` starts the stack locally.
- Re-ran final Docker Compose startup and endpoint checks after cleanup.

- Tested Nginx health routes:
  - `GET /health/identity`
  - `GET /health/sessions`
  - `GET /health/notifications`
- Tested starter endpoints:
  - `GET /api/v1/profiles`
  - `POST /api/v1/sessions`
  - `GET /api/v1/sessions`
  - `POST /api/v1/notifications`
  - `GET /api/v1/notifications`
  - `GET /api/v1/notifications/profile/1`

### Blockers
- None

### Next step
- Mark PR #4 ready for review if no final feedback is needed.

## Date: 2026-04-29

### Goal for today
- Start Sprint 2 authentication work.
- Add the first Identity service auth foundation.

### What I completed
- Created Issue #5 for Identity auth foundation work.
- Created branch `feature/identity-auth-foundation` from `feature/service-foundations`.
- Added password hashing and JWT dependencies.
- Added JWT settings for secret, algorithm, and access token expiration.
- Added password hashing helpers.
- Added JWT create/decode helpers.
- Added auth schemas for register, login, token response, and current user response.
- Added register endpoint.
- Added login endpoint.
- Added current user endpoint using bearer token auth.
- Fixed missing email validation dependency.
- Pinned bcrypt for passlib compatibility.
- Pushed the Sprint 2 auth branch.

### Issues worked on
- #5 Add Identity auth foundation

### Branches / PRs updated
- Branch: `feature/identity-auth-foundation`
- Commits:
  - `1df9b53 feat(auth): add identity auth helpers`
  - `f5f84a4 feat(auth): add register login and current user routes`
  - `e911308 fix(auth): add email validation dependency`
  - `39c8002 fix(auth): pin bcrypt for password hashing`

### Services touched
- Identity & Profile Service

### Endpoints completed
- `POST /api/v1/auth/register`
- `POST /api/v1/auth/login`
- `GET /api/v1/auth/me`

### Gateway / auth / integration completed
- Added JWT access token creation.
- Added password hashing and verification.
- Verified auth endpoints through Nginx.

### Testing / CI completed
- Confirmed Python files compile.
- Confirmed Docker Compose stack builds and starts locally.
- Tested `POST /api/v1/auth/register`.
- Tested `POST /api/v1/auth/login`.
- Tested `GET /api/v1/auth/me` with bearer token.

### Blockers
- None

### Next step
- Open Draft PR for Issue #5.
- Continue Sprint 2 with refresh token and TOTP MFA work.

## Date: 2026-04-30

### Goal for today
- Start the refresh token flow for Sprint 2.
- Make login return both access and refresh tokens.

### What I completed
- Created Issue #7 for refresh token flow.
- Created branch `feature/refresh-token-flow` from `feature/identity-auth-foundation`.
- Added refresh token expiration setting.
- Added refresh token creation helper.
- Added token type field to JWT payloads.
- Updated login response schema to include a refresh token.
- Updated login endpoint to return both access and refresh tokens.
- Added refresh token request schema.
- Added access token response schema.
- Added `POST /api/v1/auth/refresh`.
- Added refresh token validation.
- Confirmed the refresh endpoint rejects access tokens.
- Pushed the refresh token branch.
- Opened Draft PR for refresh token work.
- Pushed the completed refresh endpoint work.

### Issues worked on
- #7 Add refresh token flow

### Branches / PRs updated
- Branch: `feature/refresh-token-flow`
- Commit: `733cb8f feat(auth): issue refresh token on login`
- Commit: `6cd2426 feat(auth): add refresh token endpoint`

### Services touched
- Identity & Profile Service

### Endpoints completed
- Updated `POST /api/v1/auth/login`
- `POST /api/v1/auth/refresh`

### Gateway / auth / integration completed
- Login now returns both access and refresh tokens.
- Refresh endpoint validates refresh tokens and returns a new access token.
- Refresh endpoint rejects non-refresh tokens.

### Testing / CI completed
- Confirmed Python files compile.
- Confirmed Docker Compose stack builds and starts locally.
- Tested `POST /api/v1/auth/refresh` with a valid refresh token.
- Tested `POST /api/v1/auth/refresh` rejects an access token.

### Blockers
- None

### Next step
- Continue Sprint 2 with TOTP MFA setup and verification.

## Date: 2026-05-01
### Goal for today
- Add the first MFA flow for the Identity & Profile Service.

### Work completed
- Created the `feature/totp-mfa` branch for Issue #9.
- Added TOTP MFA setup and verification endpoints.
- Added `pyotp` as the TOTP dependency.
- Added MFA request and response schemas.
- Reused bearer token auth to protect the MFA routes.
- Updated `/auth/me` auth handling so refresh tokens are not accepted as access tokens.
- Tested the MFA flow through Nginx with register, login, setup, invalid verify, valid verify, and `/auth/me`.
- Pushed the branch and opened a draft PR.

## Date: 2026-05-03
### Goal for today
- Finish the Sprint 2 MFA work by adding a disable flow.

### Work completed
- Created Issue #11 for disabling MFA.
- Closed duplicate Issue #12.
- Created the `feature/mfa-disable` branch from `feature/totp-mfa`.
- Added `POST /api/v1/mfa/disable`.
- Required bearer token auth and a valid current TOTP code before disabling MFA.
- Cleared the stored TOTP secret after MFA is disabled.
- Updated the user MFA status so `totp_enabled` becomes false.
- Tested the full MFA lifecycle through Nginx with register, login, setup, verify, invalid disable, valid disable, second disable, and `/auth/me`.
- Pushed the branch and opened a draft PR.
- Shut down Docker Compose after testing.

### Notes
- Issue #11 completes the Sprint 2 MFA lifecycle work.
