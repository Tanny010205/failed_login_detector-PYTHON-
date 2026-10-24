
# Python Failed Login Detector

## About
A beginner-friendly cybersecurity project that analyzes
simulated authentication logs and detects repeated failed
login attempts by IP address.

## Features
- Reads authentication logs from a text file.
- Counts failed login attempts by IP address.
- Flags IP addresses that reach a configurable threshold.
- Handles a missing input file.

## Technologies
- Python 3
- File handling
- Loops and conditional statements
- collections.Counter

## Project Structure
- main.py: Main detection program.
- sample_logs.txt: Fictional login records.
- README.md: Project documentation.

## How to Run
1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run: python main.py

## Detection Rule
The default threshold is three failed login attempts.
An IP address with three or more failures triggers a warning.

## Limitations
This project uses simulated logs and a basic threshold.
A warning does not prove that an IP address is malicious.

## Future Improvements
- Detect repeated failures within a time window.
- Export reports to CSV.
- Add unit tests.
- Create a dashboard for log analysis.

## Disclaimer
For educational and defensive security learning only.
Use authorized data and systems.
