# Shyft.to Callback Manager

This script provides a command-line interface to manage callbacks for the Shyft.to API. It allows users to create, update, pause, resume, and remove callbacks, as well as manage addresses associated with these callbacks.

## Features

- Create new callbacks
- Add or remove addresses from existing callbacks
- Pause and resume callbacks
- Update callback settings
- List all registered callbacks
- Secure API key management

## Prerequisites

- Python 3.6 or higher
- `requests` library

## Installation

1. Clone this repository:

git clone https://github.com/RebornBeat/Shyft-Callback-Manager.git

cd shyft-callback-manager

2. Install the required Python package:

pip install requests

## Usage

1. Run the script:

python callbackManager.py

2. On first run, you will be prompted to enter your Shyft.to API key. This key will be saved in a file named `api_key.json` in the same directory as the script for future use.

3. Follow the on-screen prompts to manage your callbacks. The available options are:
- Create a callback
- Remove an address
- Add an address
- Pause a callback
- Resume a callback
- Remove a callback
- Update a callback
- List callbacks
- Exit

## Security Note

The API key is stored in a local file (`api_key.json`). Ensure this file is kept secure and not shared or committed to public repositories.

## License

[MIT](https://choosealicense.com/licenses/mit/)
