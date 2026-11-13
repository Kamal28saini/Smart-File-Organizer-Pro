
from pathlib import Path

APP_NAME = "Smart File Organizer Pro"
APP_VERSION = "1.0.0"

BASE_DIR = Path(__file__).resolve().parent

DATABASE_PATH = BASE_DIR / "organizer.db"
LOG_DIRECTORY = BASE_DIR / "logs"

LOG_DIRECTORY.mkdir(exist_ok=True)

FILE_CATEGORIES = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"
    ],
    "Documents": [
        ".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx",
        ".xls", ".xlsx", ".csv"
    ],
    "Videos": [
        ".mp4", ".mkv", ".mov", ".avi", ".webm"
    ],
    "Audio": [
        ".mp3", ".wav", ".aac", ".flac", ".m4a"
    ],
    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz"
    ],
    "Code": [
        ".py", ".java", ".cpp", ".c", ".js", ".html",
        ".css", ".json", ".xml", ".sql"
    ]
}

DEFAULT_CATEGORY = "Others"
