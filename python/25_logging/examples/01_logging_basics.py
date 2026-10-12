"""Logging basics: levels, handlers, formatters.

Run:
    python python/25_logging/examples/01_logging_basics.py

Also writes to python/25_logging/examples/sample.log so you can inspect
the file output.
"""

import logging
from pathlib import Path


LOG_FILE = Path(__file__).parent / "sample.log"


def setup_logger() -> logging.Logger:
    """Configure a named logger with both console and file handlers."""
    logger = logging.getLogger("demo")
    logger.setLevel(logging.DEBUG)

    # Avoid duplicate handlers when the module is re-imported
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)

    file_handler = logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(file_handler)

    return logger


def main() -> None:
    logger = setup_logger()

    print("=== Emitting one message per level ===")
    logger.debug("debug — only in the file")
    logger.info("info — visible on console and in the file")
    logger.warning("warning — something to keep an eye on")
    logger.error("error — something broke but we kept going")
    logger.critical("critical — something broke badly")

    print(f"\n=== Log file written to: {LOG_FILE} ===")
    print("=== Contents of log file: ===")
    if LOG_FILE.exists():
        print(LOG_FILE.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
