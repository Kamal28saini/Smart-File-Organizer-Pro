
from pathlib import Path
from config import FILE_CATEGORIES, DEFAULT_CATEGORY


def get_category(file_path):
    extension = Path(file_path).suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return DEFAULT_CATEGORY


def scan_files(folder_path):
    folder = Path(folder_path).expanduser()

    if not folder.exists():
        raise FileNotFoundError("Folder does not exist.")

    if not folder.is_dir():
        raise NotADirectoryError("Selected path is not a folder.")

    files = []

    for item in folder.iterdir():

        if item.is_file():

            try:
                files.append({
                    "name": item.name,
                    "path": str(item.resolve()),
                    "category": get_category(item),
                    "size": item.stat().st_size
                })

            except OSError:
                continue

    return sorted(
        files,
        key=lambda item: item["name"].lower()
    )
