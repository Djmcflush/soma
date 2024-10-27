# Soma

Soma is a Python package that enables streaming data from one location to another using sockets. It provides a simple command-line interface to send and receive data seamlessly.

This project is inspired by SOMA, the video game, and aims to bring some of its innovative concepts into the realm of data streaming.

## Features

- Stream data from a source to a destination.
- Easy installation via `pip`.
- Command-line usage with simple commands.

## Installation

You can install Soma using `pip`:

```bash
pip install .
```

Alternatively, to install it in editable mode during development:

```bash
pip install -e .
```

## Usage

After installation, you can use Soma via the command line. The general syntax is:

```bash
soma <source_file_path> <destination_file_path> [--host <host>] [--port <port>]
```

or

```bash
soma <source_file_path> --to <destination_file_path> [--host <host>] [--port <port>]
```

### Example

To stream data from `source_data.txt` to `destination_data.txt`:

```bash
soma source_data.txt destination_data.txt
```

or

```bash
soma source_data.txt --to destination_data.txt
```

### Command-Line Arguments

- `<source_file_path>`: Path to the source file.
- `<destination_file_path>`: Path to save the received file.
- `--host`: Host address (default: `localhost`).
- `--port`: Port number (default: `5000`).

## Project Structure

```
src/
└── soma/
    ├── __init__.py
    └── main.py
tests/
└── test_soma.py
.gitignore
LICENSE
README.md
requirements.txt
setup.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.
