
# Smart File Organizer Pro

A Python desktop application that automatically organizes files,
detects duplicate files, and maintains operation history.

## Features

- Automatic file categorization
- SHA-256 duplicate detection
- SQLite operation history
- Undo last file move
- Tkinter desktop GUI
- File scanning
- File preview
- Operation logging
- Collision-safe file naming
- Unit testing

## Technology Stack

- Python 3.14
- Tkinter
- SQLite
- hashlib
- pathlib
- shutil
- unittest

## Project Structure

```text
Smart-File-Organizer-Pro/
├── main.py
├── config.py
├── requirements.txt
├── src/
├── gui/
├── tests/
├── assets/
└── logs/
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Smart-File-Organizer-Pro.git

cd Smart-File-Organizer-Pro
```

Create virtual environment:

```bash
python3 -m venv .venv
```

Activate environment:

```bash
source .venv/bin/activate
```

Run application:

```bash
python main.py
```

## Testing

```bash
python -m unittest discover -s tests -v
```

## Safety

Test the application using a sample directory first.
The application moves files rather than deleting them.

## Future Improvements

- Modern GUI using CustomTkinter
- Batch undo
- File preview improvements
- File size statistics dashboard
- Export operation history
- Drag and drop support

## Author

Your Name

## License

MIT License
