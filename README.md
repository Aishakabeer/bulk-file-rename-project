# Bulk File Renamer - Python Django Application

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.1-green.svg)
![FileIO](https://img.shields.io/badge/File-Handling-ff69b4.svg)
![Regex](https://img.shields.io/badge/Regex-Enabled-orange.svg)

## Overview

A web-based tool for batch renaming files using patterns and regular expressions. Perfect for organizing photos, documents, and media collections.

## Features

### Intuitive File Management
- **Visual folder browser** - Navigate directories with a graphical interface
- **Multi-select operations** - Rename hundreds of files in one action
- **Live preview** - See changes before applying them
- **Undo functionality** - Revert renames if needed

### Advanced Renaming Options
| Mode | Example | Use Case |
|------|---------|----------|
| Pattern | `IMG_001.jpg` → `Vacation_001.jpg` | Simple replacements |
| Regex | `DSC(\d+).jpg` → `Photo_\1.png` | Complex patterns |
| Sequence | `File_1.txt`, `File_2.txt`... | Numbered series |
| Case | `document.pdf` → `DOCUMENT.PDF` | Format standardization |

### Technical Highlights
- Recursive directory processing
- File type filtering (images, docs, etc.)
- Conflict detection (prevents overwrites)
- Progress tracking for large batches

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/bulk-file-renamer.git
   cd bulk-file-renamer
Set up virtual environment:

bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
Install dependencies:

bash
pip install -r requirements.txt
Run the development server:

bash
python manage.py runserver
Access the application:

text
http://localhost:8000
