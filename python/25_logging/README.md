# Module 25 — Logging

`print()` is for debugging by yourself. `logging` is for understanding
what your program is doing in production, at 3 AM, when you're not at
the keyboard.

## Concepts covered

- **Why logging beats print** — levels, timestamps, sources, filtering.
- **Log levels** — DEBUG, INFO, WARNING, ERROR, CRITICAL.
- **The root logger** and named loggers (`logging.getLogger(__name__)`).
- **Handlers** — console, file, rotating file.
- **Formatters** — line layout, timestamps, function names.
- **Configuration** — `basicConfig`, `dictConfig`, YAML/JSON config.
- **Logging in data pipelines** — one logger per module, contextual fields.
- **Structured logging** — JSON logs for machine consumption.
- **What not to log** — PII, secrets, huge payloads.

## Data Science connection

Long-running training jobs, ETL pipelines, API ingestion — you need a
log trail showing what ran, when, on what data, with what result. Logs
are how you debug a model that trained three weeks ago and produced
nonsense.

## References

- Python docs — logging: https://docs.python.org/3/library/logging.html
- Python docs — logging cookbook: https://docs.python.org/3/howto/logging-cookbook.html
