```txt
▗▖ ▗▖▗▞▀▜▌▄▄▄▄  ▄▄▄▄  ▗▞▀▜▌▄▄▄▄  
▐▌ ▐▌▝▚▄▟▌█   █ █ █ █ ▝▚▄▟▌█   █ 
▐▛▀▜▌     █   █ █   █      █   █ 
▐▌ ▐▌         ▗▄▖                
             ▐▌ ▐▌               
              ▝▀▜▌               
             ▐▙▄▞▘               
```

This repository contains a lightweight, pure Python implementation of the classic game Hangman.

## Project Struckture

```bash
.
├── img                 # ASCII-Art assets for game states
├── LICENSE             # Project license (MIT)
├── README.md           # Project documentation
└── src                 # Source code
    ├── hangman.py      # Main entry point
    ├── mvp             # Minimum Viable Product
    └── poc             # Proof of Concept
```

## Installation & Setup

### Prerequisites

- Python 3.9 or higher

### 1. Clone Repository & Setup Environment

First, clone the repository and navigate into the folder. Although this project has no external dependencies yet, using a virtual environment is recommended as a best practice.

```bash
# Create a virtual environment
python -m venv .venv

# Activation for Linux/macOS
source .venv/bin/activate

# Activation for Windows
.venv\Scripts\activate
```

### 2. Install Dependencies

> Note: The current version uses only the Python Standard Library. No installation of external packages is required at this stage.

```bash
# Optional: only needed if requirements.txt exists for future updates
pip install -r requirements.txt
```

## How to Play

To start the game, simply run the main script from your terminal:

```bash
python3 src/hangman.py
```

## License

This project is licensed under the MIT License.
