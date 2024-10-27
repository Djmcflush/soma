# Soma

Soma is a Python package that enables streaming data from one location to another using sockets. It provides a simple command-line interface to send and receive data seamlessly.

This project is inspired by SOMA, the video game, in which the main protaginist eventually learns how data transfer works.


## A Revelation on Data Transfer

While building this project, I had a fundamental realization about how data movement truly works. I was initially trying to find a way to **stream data from point A to point B** without ever duplicating it — to literally move the data so that it exists in only one place at any given time. However, I came to understand that:

### There Is No Way to Truly Move Data Without Temporary Duplication

Fundamentally, when data is moved between locations — whether it's across storage devices, over a network, or even between different memory areas — it must be **read** from the source and **written** to the destination. During this process, **at some point in time, the data exists in both locations**, even if only briefly.

This happens because:

- **Reading and Writing**: Data needs to be read from the original location and written to the new one. This inherently means that, for at least a moment, data is present in two places.
- **Atomicity and Safety**: Temporary duplication is necessary to ensure **data integrity**. If data were to disappear from the source before being fully written to the destination, any failure during the transfer would lead to data loss.
- **Pipes and Streams**: Even using **pipes** or **streaming** techniques, there is always some form of **buffering** happening, meaning that data is temporarily duplicated to facilitate the transfer.

This realization was enlightening: despite all our technological advances, the basic laws of **data transfer** remain rooted in reading and writing, and we cannot avoid temporary duplication without compromising reliability.

I wanted to share this insight because it reshaped my understanding of data movement and how we think about **efficiency** and **safety** when handling data transfers. Understanding this can help in designing better systems that respect the fundamental limits of data storage and transmission.


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
