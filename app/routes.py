from flask import Blueprint, jsonify, request
from .data_analysis import get_bid_statistics, get_ask_statistics, get_general_statistics
from .blockchain_api import fetch_order_book

bp = Blueprint('api', __name__)

@bp.route('/load_data/<symbol>', methods=['GET'])
def load_data(symbol):
    """
    Endpoint to load and return order book data for a given cryptocurrency symbol.
    
    Args:
        symbol (str): The cryptocurrency symbol to fetch data for (e.g., 'BTC-USD').

    Returns:
        Response: JSON data of the order book for the given symbol.
    """
    data = fetch_order_book(symbol)
    return jsonify(data), 200

@bp.route('/bids/<symbol>', methods=['GET'])
def bids(symbol):
    """
    Endpoint to get statistics for bids of a given cryptocurrency symbol.

    Args:
        symbol (str): The cryptocurrency symbol to fetch bid statistics for.

    Returns:
        Response: JSON data containing statistics for bids.
    """
    data = fetch_order_book(symbol)
    if 'bids' in data:
        stats = get_bid_statistics(data['bids'])
        return jsonify({'bids': stats}), 200
    else:
        return jsonify({'error': 'No bid data available'}), 404

@bp.route('/asks/<symbol>', methods=['GET'])
def asks(symbol):
    """
    Endpoint to retrieve statistics for asks of a given cryptocurrency symbol.
    
    Args:
        symbol (str): Cryptocurrency symbol pair (e.g., 'BTC-USD').

    Returns:
        Response: JSON response containing the asks statistics.
    """
    data = fetch_order_book(symbol)
    if 'asks' in data:
        stats = get_ask_statistics(data['asks'])
        return jsonify({'asks': stats}), 200
    else:
        return jsonify({'error': 'No ask data available'}), 404

@bp.route('/general_stats/<symbol>', methods=['GET'])
def general_stats(symbol):
    """
    Endpoint to retrieve combined general statistics for bids and asks
    of a given cryptocurrency symbol.
    
    Args:
        symbol (str): Cryptocurrency symbol pair (e.g., 'BTC-USD').

    Returns:
        Response: JSON response containing combined statistics for bids and asks.
    """
    data = fetch_order_book(symbol)
    stats = get_general_statistics(data)
    return jsonify(stats), 200
