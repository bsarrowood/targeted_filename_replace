# Targeted Filename Replacement Tool

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A powerful Python script for batch renaming files with multiple operation modes, designed specifically for media server preparation and file organization.

## Features

- **Three Renaming Modes**:
  - 🔄 Standard text replacement
  - 🔝 Prefix addition (header)
  - ⏸️ Precise text injection at calculated positions
- **Safety First**:
  - 👁️ Preview all changes before execution
  - ❌ Conflict prevention for incompatible modes
  - ✔️ Confirmation prompt for recursive operations
- **Flexible Processing**:
  - 📂 Single folder or recursive subfolder operation
  - 💻 Cross-platform (Windows/macOS/Linux)

## Installation

1. Ensure Python 3.6+ is installed
2. Download `targeted_filename_replace.py`
3. Run directly: `python targeted_filename_replace.py`

## Usage

### Basic Configuration
```python
# Required
folder_path = r"C:\Media\TV Shows\Arrow"  # Raw string for Windows paths
text_to_find = "Arrow.S01E"               # Text to find/replace
replacement_text = "Arrow - s01e"         # Replacement text

# Options
recursive = False       # Process subfolders (True/False)
add_as_header = False   # Add as prefix instead of replacing
injection = False       # Inject at calculated position
