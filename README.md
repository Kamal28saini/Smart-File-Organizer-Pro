# 📁 Smart File Organizer Pro

<p align="center">
  <img src="screenshots/dashboard.png" width="800" alt="Smart File Organizer Pro Dashboard">
</p>

<p align="center">
  <strong>A Python Desktop Application for Intelligent File Organization</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14+-blue?logo=python">
  <img src="https://img.shields.io/badge/GUI-Tkinter-orange">
  <img src="https://img.shields.io/badge/Database-SQLite-green">
  <img src="https://img.shields.io/badge/License-MIT-yellow">
</p>

## 🚀 Overview

Smart File Organizer Pro is a desktop application developed using Python that automatically organizes files into categories based on their extensions.

It provides an intuitive graphical interface for file management, duplicate detection, operation history, and undo functionality.

## ✨ Features

- 📂 Automatic file organization by file type
- 🖼️ Image, document, video, audio, archive, and code categorization
- 🔍 Duplicate file detection using SHA-256 hashing
- ↩️ Undo the last file organization operation
- 📜 File operation history using SQLite
- 📊 Interactive desktop dashboard using Tkinter
- 📝 Application logging
- 🔎 File scanning and preview
- ⚡ Collision-safe file movement

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application development |
| Tkinter | Graphical user interface |
| SQLite | Operation history database |
| hashlib | Duplicate detection |
| pathlib | File path management |
| shutil | File movement |
| logging | Application logging |
| unittest | Unit testing |

## 📁 Project Structure

```text
Smart-File-Organizer-Pro/
├── main.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
├── src/
│   ├── file_scanner.py
│   ├── organizer.py
│   ├── duplicate_detector.py
│   ├── database.py
│   └── logger.py
├── gui/
│   └── dashboard.py
├── tests/
│   └── test_organizer.py
├── screenshots/
│   └── dashboard.png
└── logs/
```

## 💻 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Kamal28saini/Smart-File-Organizer-Pro.git
cd Smart-File-Organizer-Pro
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the environment

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python main.py
```

### macOS Tkinter Setup

For Homebrew Python 3.14:

```bash
brew install python-tk@3.14
```

## 🧪 Run Tests

```bash
python -m unittest discover -s tests -v
```

## 📌 Usage

1. Launch Smart File Organizer Pro.
2. Select a folder using the Browse button.
3. Scan files in the selected folder.
4. Review the detected files and categories.
5. Organize files into category folders.
6. Find duplicate files when required.
7. Undo the last organization operation if needed.
8. Review operation history.

## 🔮 Future Enhancements

- File preview improvements
- Advanced duplicate management
- Drag-and-drop support
- File organization scheduling
- Advanced search and filtering
- Improved dashboard analytics
- Cross-platform executable packaging

## 👨‍💻 Author

**Kamal Saini**

GitHub: [@Kamal28saini](https://github.com/Kamal28saini)

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub!

## 📄 License

This project is intended to be released under the MIT License. See the `LICENSE` file for details.
