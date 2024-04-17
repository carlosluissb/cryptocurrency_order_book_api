import requests
import os
from dotenv import load_dotenv
import os

def fetch_order_book(symbol):
    """
    Fetch order book data for a given symbol from the blockchain API.

    Args:
        symbol (str): The symbol to fetch order book data for.

    Returns:
        dict: The order book data fetched from the blockchain API.
    """
    load_dotenv()
    api_key = os.getenv('BLOCKCHAIN_API_KEY')
    print(api_key)
    url = f'https://api.blockchain.com/v3/exchange/l3/{symbol}'
    headers = {
        'X-API-Token': api_key
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        return response.json()
    except requests.RequestException as e:
        return {'error': f'Failed to fetch data: {str(e)}'}
