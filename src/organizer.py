
import shutil
from pathlib import Path

from src.file_scanner import get_category
from src.database import (
    record_move,
    get_last_move,
    mark_undone
)
from src.logger import logger


def get_unique_path(destination):

    destination = Path(destination)

    if not destination.exists():
        return destination

    parent = destination.parent
    stem = destination.stem
    suffix = destination.suffix

    counter = 1

    while True:

        new_path = parent / f"{stem}_{counter}{suffix}"

        if not new_path.exists():
            return new_path

        counter += 1


def organize_files(file_paths):

    moved_count = 0
    errors = []

    for file_path in file_paths:

        source = Path(file_path)

        if not source.is_file():
            continue

        category = get_category(source)

        destination_folder = source.parent / category

        destination_folder.mkdir(
            exist_ok=True
        )

        destination = get_unique_path(
            destination_folder / source.name
        )

        try:

            shutil.move(
                str(source),
                str(destination)
            )

            record_move(
                source,
                destination
            )

            logger.info(
                "Moved %s to %s",
                source,
                destination
            )

            moved_count += 1

        except OSError as error:

            errors.append(
                f"{source.name}: {error}"
            )

            logger.error(
                "Failed to move %s: %s",
                source,
                error
            )

    return moved_count, errors


def undo_last_move():

    operation = get_last_move()

    if operation is None:
        return False

    operation_id, original_path, destination_path = operation

    source = Path(destination_path)
    destination = Path(original_path)

    if not source.exists():
        return False

    if destination.exists():
        return False

    try:

        destination.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        shutil.move(
            str(source),
            str(destination)
        )

        mark_undone(operation_id)

        logger.info(
            "Undo completed: %s",
            destination
        )

        return True

    except OSError as error:

        logger.error(
            "Undo failed: %s",
            error
        )

        return False
