# SDKMAN Interactive CLI

An interactive command-line interface for SDKMAN (Software Development Kit Manager), making it easier to browse, filter, and install SDKs.

[中文文档](README.zh-CN.md)

## Features

- Interactive version selection with formatted display
- Version filtering by keyword (e.g., "21" for Java 21)
- Support for all SDKMAN candidates (Java, Kotlin, Gradle, etc.)
- Comprehensive command-line interface
- User-friendly display of version information

## Prerequisites

- Python 3.6+
- SDKMAN installed and configured
- Bash shell environment

## Installation

Clone this repository:

```bash
git clone https://github.com/yourusername/sdkman-mcp.git
cd sdkman-mcp
```

## Usage

### As a Python Module

```python
from src.sdkman_mcp.sdk_commands import sdk_interactive_install

# Install Java with interactive selection
result = sdk_interactive_install("java")

# Install Java 21.x with filtering
result = sdk_interactive_install("java", "21")
```

### Command Line Interface

The package provides ready-to-use scripts:

#### General SDK Installer

Install any SDKMAN candidate:

```bash
python examples/install_sdk.py java       # Install any Java version
python examples/install_sdk.py java 21    # Install Java 21.x
python examples/install_sdk.py kotlin     # Install Kotlin
python examples/install_sdk.py gradle 8   # Install Gradle 8.x
```

#### JDK-specific Installer

```bash
python examples/install_jdk.py           # Install any JDK version
python examples/install_jdk.py 21        # Install JDK 21.x
```

### Main CLI

The module can also be run directly:

```bash
python -m src.sdkman_mcp.sdk_commands install java --version 21
python -m src.sdkman_mcp.sdk_commands list java
python -m src.sdkman_mcp.sdk_commands current
```

## Example Output

When running the interactive installer, you'll see a formatted list of available versions:

```
=========================================================================
Available java versions (filter: '21') - 12 results
=========================================================================
Number Vendor       | Use  | Version    | Dist      | Status      | Identifier
------ ------------ | ---- | ---------- | --------- | ----------- | -------------------------
1      Correto      |      | 21.0.7     | amzn      |             | 21.0.7-amzn
2      Correto      |      | 21.0.6     | amzn      |             | 21.0.6-amzn
3      GraalVM CE   |      | 21.0.2     | graalce   |             | 21.0.2-graalce
4      GraalVM Oracle|     | 21.0.7     | graal     |             | 21.0.7-graal
5      GraalVM Oracle|     | 21.0.6     | graal     |             | 21.0.6-graal
6      Java.net     |      | 21.0.2     | open      |             | 21.0.2-open
7      Liberica     |      | 21.0.7.fx  | librca    |             | 21.0.7.fx-librca
8      Liberica     |      | 21.0.7     | librca    |             | 21.0.7-librca
9      Liberica     |      | 21.0.6.fx  | librca    |             | 21.0.6.fx-librca
10     Liberica     |      | 21.0.6     | librca    |             | 21.0.6-librca

Note: >>> in the Use column indicates the current default version

Please select a version number (or enter 'q' to exit): 
```

## API Reference

The module provides several functions:

- `sdk_interactive_install(candidate, search_version=None)`: Interactive installation
- `parse_sdk_versions(output, search_version=None)`: Parse SDK version list
- Other standard SDKMAN functions (list, install, current, etc.)

## How It Works

The tool provides an enhanced interface for SDKMAN by:

1. Executing SDKMAN commands through the shell
2. Parsing and formatting the output
3. Providing an interactive interface for selection
4. Handling installation with proper confirmation steps

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [SDKMAN](https://sdkman.io/) - The Software Development Kit Manager
- All contributors to this project 