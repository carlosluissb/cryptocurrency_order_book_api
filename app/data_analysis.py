import pandas as pd


def calculate_statistics(orders):
    """
    Calculate various statistics from order data.
    
    Args:
        orders (list of dicts): Order data, where each order is a dictionary 
                                with 'px' (price) and 'qty' (quantity).

    Returns:
        dict: Calculated statistics including average value, greatest value, 
              least value, total quantity, and total price.
    """ 
    if not orders:
        return {}
    df = pd.DataFrame(orders)
    df['value'] = df['px'] * df['qty']

    result = {
        'average_value': df['value'].mean(),
        'greater_value': df.loc[df['value'].idxmax()].to_dict(),
        'lesser_value': df.loc[df['value'].idxmin()].to_dict(),
        'total_qty': df['qty'].sum(),
        'total_px': df['px'].sum()
    }
    return result

def get_general_statistics(data):
    """
    Compute general statistics for bids and asks.

    Args:
        data (dict): Data containing 'bids' and 'asks' which are lists of orders.

    Returns:
        dict: Statistics for both bids and asks including count, quantity, 
              and total value.
    """
    general_stats = {}
    if 'bids' in data:
        bids_df = pd.DataFrame(data['bids'])
        bids_stats = {
            'count': len(bids_df),
            'qty': bids_df['qty'].sum(),
            'value': (bids_df['px'] * bids_df['qty']).sum()
        }
    else:
        bids_stats = {'count': 0, 'qty': 0, 'value': 0}

    if 'asks' in data:
        asks_df = pd.DataFrame(data['asks'])
        asks_stats = {
            'count': len(asks_df),
            'qty': asks_df['qty'].sum(),
            'value': (asks_df['px'] * asks_df['qty']).sum()
        }
    else:
        asks_stats = {'count': 0, 'qty': 0, 'value': 0}

    general_stats = {
        'bids': bids_stats,
        'asks': asks_stats
    }
    return general_stats

def get_bid_statistics(bids):
    """
    Get statistics for bids.

    Args:
        bids (list): List of bid orders.

    Returns:
        dict: Statistics for bids.
    """
    return calculate_statistics(bids)

def get_ask_statistics(asks):
    """
    Get statistics for asks.

    Args:
        asks (list): List of ask orders.

    Returns:
        dict: Statistics for asks.
    """
    return calculate_statistics(asks)