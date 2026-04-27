## Installation
### 1. Clone the github repository
- HTTPS
    ``` bash
    git clone https://github.com/bluery0206/dost-byte-openalex.git
    ```
- SSH
    ``` bash
    git clone git@github.com:bluery0206/dost-byte-openalex.git
    ```
### 2. Installing Dependencies
- Separate virtual environment (Preferred)
    ```bash
    cd dost-byte-openalex

    # CREATING A VIRTUAL ENVIRONMENT
    # If it doesn't work or you're on linux, 
    # change `py` to `python` or `python3` 
    py -m venv .venv

    # ACTIVATING THE VIRTUAL ENVIRONMENT
    # Windows
    ./.venv/Scripts/activate

    # Linux
    source ./.venv/bin/activate

    pip install -r  requirements.txt
    ```
-  Global
    ```bash
    # If it doesn't work or you're on linux, 
    # change `py` to `python` or `python3` 
    py -m pip install -r  requirements.txt
    ```