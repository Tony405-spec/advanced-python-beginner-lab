"""Structured logging — JSON output for machine consumption.

Run:
    python python/25_logging/examples/02_structured_logging.py

Structured logs (usually JSON, one object per line) are how modern
observability stacks (ELK, Datadog, Loki, CloudWatch) ingest logs.
Human-readable on one side, queryable on the other.
"""

import json
import logging
import sys
from datetime import datetime, timezone


class JsonFormatter(logging.Formatter):
    """Formatter that emits one JSON object per log record."""

    def format(self, record: logging.LogRecord) -> str:
        payload = {
            "timestamp": datetime.fromtimestamp(
                record.created, tz=timezone.utc
            ).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }

        skip = {
            "name", "msg", "args", "levelname", "levelno", "pathname",
            "filename", "module", "exc_info", "exc_text", "stack_info",
            "lineno", "funcName", "created", "msecs", "relativeCreated",
            "thread", "threadName", "processName", "process",
            "taskName", "message", "asctime",
        }
        for key, value in record.__dict__.items():
            if key in payload or key.startswith("_") or key in skip:
                continue
            try:
                json.dumps(value)
                payload[key] = value
            except (TypeError, ValueError):
                payload[key] = repr(value)

        if record.exc_info:
            payload["exception"] = self.formatException(record.exc_info)

        return json.dumps(payload, ensure_ascii=False)


def setup_logger(name: str = "pipeline") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    if logger.handlers:
        return logger
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JsonFormatter())
    logger.addHandler(handler)
    return logger


def main() -> None:
    logger = setup_logger()

    print("=== Basic structured records ===")
    logger.info("pipeline started")
    logger.warning("slow query detected")

    print("\n=== Structured fields via extra= ===")
    logger.info(
        "batch processed",
        extra={"batch_id": "b-001", "rows": 12_345, "duration_ms": 842},
    )

    logger.error(
        "row failed validation",
        extra={
            "row_index": 42,
            "column": "age",
            "value": -3,
            "reason": "must be non-negative",
        },
    )

    print("\n=== Each line above is a parseable JSON object ===")


if __name__ == "__main__":
    main()
