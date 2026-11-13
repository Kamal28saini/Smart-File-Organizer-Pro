
import hashlib
from pathlib import Path


def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(
            lambda: file.read(1024 * 1024),
            b""
        ):
            sha256.update(chunk)

    return sha256.hexdigest()


def find_duplicates(file_paths):

    hash_map = {}

    for file_path in file_paths:

        path = Path(file_path)

        if not path.is_file():
            continue

        try:
            file_hash = calculate_hash(path)

            hash_map.setdefault(
                file_hash,
                []
            ).append(str(path.resolve()))

        except OSError:
            continue

    return {
        file_hash: paths
        for file_hash, paths in hash_map.items()
        if len(paths) > 1
    }
