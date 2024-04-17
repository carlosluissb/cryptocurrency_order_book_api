# tests/test_data_analysis.py

import unittest
from app.data_analysis import calculate_statistics, get_general_statistics

class TestDataAnalysis(unittest.TestCase):
    def test_calculate_statistics(self):
        '''
        test data
        '''
        orders = [
            {'px': 100, 'qty': 2},
            {'px': 200, 'qty': 1.5},
            {'px': 50, 'qty': 4}
        ]
        
        stats = calculate_statistics(orders)
        
        self.assertEqual(stats['average_value'], 700 / 3)
        self.assertEqual(stats['total_qty'], 7.5)
        self.assertEqual(stats['total_px'], 350)
        self.assertEqual(stats['greater_value']['value'], 300)
        self.assertEqual(stats['lesser_value']['value'], 200)

    def test_general_statistics(self):
        '''
        test data
        '''
        orders = {
        'symbol': 'BTC-USD', 'bids': [{'px': 100, 'qty': 2},], 'asks':[{'px': 200, 'qty': 4}, ]
        }
        
        stats = get_general_statistics(orders)       
        self.assertEqual(stats['bids'], {'count': 1, 'qty': 2, 'value': 200})
        self.assertEqual(stats['asks'], {'count': 1, 'qty': 4, 'value': 800})
        

if __name__ == '__main__':
    unittest.main()
