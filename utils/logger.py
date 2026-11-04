import logging
import pathlib

LOG_DIR = pathlib.Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("automation")
logger.setLevel(logging.INFO)

if not logger.handlers:
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler = logging.FileHandler(
        LOG_DIR / "automation.log",
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)