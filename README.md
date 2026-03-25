# CI Release Platform

A GitHub-based CI and release control platform, built incrementally over several weeks.

---

## Purpose

This repository is the first stage of a larger portfolio project. The long-term goal is to build:

- A GitHub-based CI and release control platform
- Protected exact release branches (`rc/1.0.0`, `rc/1.0.1`, `rc/1.1.0`, …)
- Automatic candidate builds on merges to `rc` branches
- Manual promotion of the tip of an `rc` branch to a final release tag
- Later integration with Azure-based validation and reporting services

---

## Week 1 Scope

This phase delivers a minimal, production-style scaffold:

- A small **Python 3.11 FastAPI** service with `/health` and `/version` endpoints
- **Unit and API tests** via pytest, with coverage and JUnit XML output
- **Linting** with flake8
- **GitHub Actions CI** that runs on every relevant push and pull request
- A basic **Dockerfile** and **docker-compose** for local use
- This README

Release promotion, Azure Functions, and rack orchestration are **not** included yet.

---

## Branch Naming

| Prefix | Purpose |
|--------|---------|
| `dev/<name>` | Feature development |
| `bug/<name>` | Bug fixes |
| `task/<name>` | Chores, refactors, documentation |
| `main` | Stable integration branch |

> `rc/x.y.z` release branches will be added in a future phase.

---

## CI Behaviour

The workflow (`.github/workflows/ci.yml`) triggers on:

- Push to `main`, `dev/**`, `bug/**`, `task/**`
- Pull requests targeting `main`

Steps:

1. Check out code
2. Set up Python 3.11
3. Install `requirements-dev.txt`
4. Run **flake8** — fails the build on any lint error
5. Run **pytest** — fails the build on any test failure
6. Upload `pytest-report.xml` as an artifact *(always, even on failure)*
7. Upload `coverage.xml` as an artifact *(always, even on failure)*
8. Zip `app/` + `requirements.txt` → upload as `package` artifact

---

## Local Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
```

---

## Running Tests

```bash
pytest
```

Output files produced:

- `pytest-report.xml` — JUnit-style test report
- `coverage.xml` — coverage report

---

## Running the App Locally

```bash
uvicorn app.main:app --reload
```

Open <http://localhost:8000/health> or <http://localhost:8000/version>.

---

## Running with Docker

```bash
docker compose up --build
```

The API will be available at <http://localhost:8000>.

---

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app creation
│   ├── api.py           # /health and /version routes
│   └── utils.py         # Reusable helpers
├── tests/
│   ├── test_api.py      # Endpoint integration tests
│   └── test_utils.py    # Utility unit tests
├── .github/
│   └── workflows/
│       └── ci.yml       # GitHub Actions CI workflow
├── requirements.txt     # Runtime dependencies
├── requirements-dev.txt # Dev/test dependencies
├── pytest.ini           # pytest configuration
├── .flake8              # flake8 configuration
├── .gitignore
├── Dockerfile
├── docker-compose.yml
└── README.md
```
