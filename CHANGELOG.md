# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2023-04-27

### Added
- Interactive version selection feature for SDK installation
- Support for filtering versions by keyword
- User-friendly formatted display of available versions
- Command-line interface for all SDKMAN operations
- Special JDK installation script (`install_jdk.py`)
- General SDK installation script (`install_sdk.py`)
- Improved shell integration with SDKMAN
- Version parsing and structured data conversion
- Multi-language documentation (English and Chinese)

### Changed
- Modified SDKMAN integration to use proper source initialization
- Enhanced output formatting for version listings

### Fixed
- Proper handling of SDKMAN environment path detection
- Shell integration with bash for proper command execution

## [0.1.0] - 2023-04-26

### Added
- Initial project structure
- Basic SDKMAN command wrappers for:
  - List, install, uninstall
  - Current version display
  - Version management
  - Configuration and environment handling 