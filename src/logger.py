
import logging
from config import LOG_DIRECTORY

LOG_FILE = LOG_DIRECTORY / "organizer.log"

logger = logging.getLogger("SmartFileOrganizer")
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8"
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)
