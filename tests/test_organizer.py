
import unittest
import tempfile
from pathlib import Path

from src.file_scanner import get_category, scan_files
from src.duplicate_detector import calculate_hash


class TestSmartFileOrganizer(unittest.TestCase):

    def test_image_category(self):

        self.assertEqual(
            get_category("photo.jpg"),
            "Images"
        )

    def test_document_category(self):

        self.assertEqual(
            get_category("report.pdf"),
            "Documents"
        )

    def test_code_category(self):

        self.assertEqual(
            get_category("main.py"),
            "Code"
        )

    def test_unknown_category(self):

        self.assertEqual(
            get_category("sample.xyz"),
            "Others"
        )

    def test_scan_files(self):

        with tempfile.TemporaryDirectory() as folder:

            path = Path(folder) / "sample.txt"

            path.write_text(
                "Hello Python",
                encoding="utf-8"
            )

            files = scan_files(folder)

            self.assertEqual(
                len(files),
                1
            )

            self.assertEqual(
                files[0]["name"],
                "sample.txt"
            )

    def test_hash_same_content(self):

        with tempfile.TemporaryDirectory() as folder:

            file1 = Path(folder) / "file1.txt"
            file2 = Path(folder) / "file2.txt"

            file1.write_text("Same content")
            file2.write_text("Same content")

            self.assertEqual(
                calculate_hash(file1),
                calculate_hash(file2)
            )


if __name__ == "__main__":

    unittest.main()
