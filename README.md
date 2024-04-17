# Cryptocurrency Order Book API

## Introduction

This API interfaces with the Blockchain.com Exchange API to fetch real-time order book data for different cryptocurrency pairs and provides statistical analysis of the bids and asks in the order book.

## Setup

1. Clone the repository to your local machine.
2. Ensure that Python 3.9+ is installed on your system.
3. Install the required dependencies by running `pip install -r requirements.txt` within the project directory.
4. Obtain an API key from Blockchain.com and set it in a `.env` file as `BLOCKCHAIN_API_KEY=your_api_key_here`.

## Running the Application

To start the application, navigate to the root directory of the project and execute the `run.py` file:

```bash
python run.py
```

This will start a Flask development server, typically on http://127.0.0.1:5000.

## Endpoints
/load_data/<symbol>: Fetch and load order book data for a given symbol (e.g., BTC-USD).
/bids/<symbol>: Retrieve statistical analysis of bids for a given symbol.
/asks/<symbol>: Retrieve statistical analysis of asks for a given symbol.
/general_stats/<symbol>: Retrieve general statistics combining both bids and asks for a given symbol.

## Examples
To get bids statistics for BTC-USD, you would send a GET request to:

Copy code
```bash
http://127.0.0.1:5000/bids/BTC-USD
```
Response:

json
Copy code
{
  "bids": {
    "average_value": ...,
    "greater_value": {...},
    "lesser_value": {...},
    "total_qty": ...,
    "total_px": ...
  }
}
Replace /bids/ with /asks/ for asks statistics, and use /general_stats/ for combined statistics.

Tests
To run tests, use the following command from the root directory:

```bash
python -m unittest discover -s tests
```

Ensure that you have a testing module and tests written as per Python's unittest framework.