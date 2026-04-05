# Changelog - AlsoPlaying

## [v1.1.0] - 2026-03-22

### Added.
- **New Feature**: Added a folder selection field to choose where generated widgets are saved (defaults to Desktop).
- **Localization**: Full support for English and Spanish with automatic system language detection.
- **Automated Setup**: 
    - Automatic detection and installation of Python (via winget) if missing or outdated.
    - Automatic verification and installation of PyInstaller.
- **Robustness**: 
    - Global exception handler to prevent silent crashes and provide detailed error messages.
    - Improved path detection logic for better compatibility with compiled environments.

### Changed
- **Modularization**: Refactored the monolithic script into a clean, modular structure:
    - `AlsoPlaying.py`: Main application logic and UI.
    - `localization.py`: Multi-language string management.
    - `resources.py`: Embedded assets (base64 icons).
    - `templates.py`: Script template for the generated widgets.
- **Requirements**: Added `requirements.txt` for easier project setup.

### Fixed
- **WinError 3**: Resolved "The system cannot find the path specified" error during the build process by improving internal path handling.
- **Encoding issues**: Fixed potential encoding problems between the modular files.

---
*Created by Fernando Guerrero Nuez*
