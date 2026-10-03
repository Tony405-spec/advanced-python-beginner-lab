# Module 24 — Testing

Tests are code that verifies code. They catch regressions, document
intent, and give you the confidence to refactor. This module is about
testing as a discipline, not just as a tool.

## Concepts covered

- **Why tests exist** — regression safety, refactoring confidence, docs.
- **Test pyramid** — unit, integration, end-to-end.
- **pytest** — the standard testing framework.
- **Fixtures** — `@pytest.fixture`, setup/teardown, scopes.
- **Parametrization** — `@pytest.mark.parametrize`.
- **Exceptions** — `pytest.raises`.
- **Mocking** — `unittest.mock`, `monkeypatch`.
- **Property-based testing** — `hypothesis` introduction.
- **Coverage** — what it measures, what it doesn't.
- **What not to test** — third-party code, trivial getters.

## Data Science connection

Data pipelines need tests for edge cases: empty DataFrames, NaN values,
unexpected dtypes, division by zero, file-not-found. A tested pipeline
is one you can run without fear at 3 AM.

## References

- pytest docs: https://docs.pytest.org/
- Fluent Python, 2nd ed., Chapter 8 (test patterns)
- Architecture Patterns with Python — Harry Percival & Bob Gregory
