# Create a Simple Stopwatch

A simple Python GUI stopwatch built with Tkinter.

## Features

- Start the stopwatch
- Stop and pause the stopwatch
- Resume timing after stopping
- Reset the stopwatch to zero
- Displays elapsed time in `HH:MM:SS` format
- Uses `time.monotonic()` for reliable elapsed-time tracking
- Includes automated tests for the timing logic

## Requirements

- Python 3.8 or later
- Tkinter

Tkinter is included with most standard Python installations on Windows.

## How to Run

Open PowerShell in the project folder and run:

    python stopwatch.py

The stopwatch window will open.

## Controls

- **Start** — Starts or resumes the stopwatch.
- **Stop** — Pauses the stopwatch while preserving the elapsed time.
- **Reset** — Resets the stopwatch to `00:00:00`.

## Running Tests

The timing logic has automated unit tests.

Run:

    python -m unittest test_stopwatch.py

## Project Structure

    Create-a-Simple-Stopwatch/
    ├── stopwatch.py
    ├── test_stopwatch.py
    ├── .gitignore
    ├── README.md
    └── LICENSE

## Author

**Hrishikesh Sharma**

GitHub: RaavanHrishi07

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.