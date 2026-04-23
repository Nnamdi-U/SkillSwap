# SkillSwap

## Project Overview
A peer skill-exchange platform where users create profiles, request learning sessions, and receive notifications when session events happen.

## Architecture Summary
SkillSwap is a backend-only microservices project built with:
- 3 FastAPI services
- Nginx as the API gateway
- Docker Compose for orchestration
- PostgreSQL for persistence
- SQLAlchemy and Pydantic for data handling


## Service Boundaries
### Identity & Profile Service
- registration, login, refresh token flow, and current user endpoint
- JWT issuance and centralized authentication
- TOTP MFA setup, verification, and disable
- profile creation, updates, and lookup
- role-based access support

### Session Service
- create, list, retrieve, and update session requests
- filter sessions by status
- validate profiles through the Identity & Profile Service
- call the Notification Service for major session events

### Notification Service
- create and list notifications
- get notifications by profile ID
- store notification delivery or status results

## Auth, MFA, and Request IDs
- Password hashing, JWT authentication, and role-based authorization are centralized in the Identity & Profile Service.
- TOTP MFA is required through setup, verify, and disable flows.
- Protected routes across services trust the centralized identity model.
- Every request must preserve or generate `X-Request-ID` and forward it across downstream service calls.
- Structured logs should include request ID, method, path, response status, downstream target, and downstream success or failure.

## Routes and Gateway
All external traffic enters through Nginx under `/api/v1/...`.

- `/api/v1/auth/*` and `/api/v1/profiles/*` route to the Identity & Profile Service
- `/api/v1/sessions/*` routes to the Session Service
- `/api/v1/notifications/*` routes to the Notification Service

Main route groups:
- auth
- MFA
- profiles
- sessions
- notifications
- health endpoints for each service

## Run, Test, and CI
Planned local startup:

```bash
docker compose up --build
```

## Known Limitations
None as of now.
