"""
Mock NSE Stock Data Generator
==============================

This module generates realistic mock NSE stock data for development and demonstration
purposes. Used when external API access is not available or for testing.

This allows the application to be peer-reviewed and demonstrated without requiring
live API access or internet connectivity.

Author: Mandar Bahadarpurkar
"""

import random
from datetime import datetime, timedelta
from typing import Dict, List
import json


class MockNSEData:
    """Generate realistic mock NSE stock market data."""
    
    # Common NSE stocks with realistic base prices
    STOCK_DATA = {
        'RELIANCE': {'base_price': 2650.50, 'volatility': 0.02, 'sector': 'Energy'},
        'TCS': {'base_price': 3850.75, 'volatility': 0.015, 'sector': 'IT'},
        'INFY': {'base_price': 1580.30, 'volatility': 0.018, 'sector': 'IT'},
        'HDFCBANK': {'base_price': 1685.90, 'volatility': 0.02, 'sector': 'Banking'},
        'ICICIBANK': {'base_price': 1150.40, 'volatility': 0.022, 'sector': 'Banking'},
        'HINDUNILVR': {'base_price': 2420.60, 'volatility': 0.012, 'sector': 'FMCG'},
        'ITC': {'base_price': 465.80, 'volatility': 0.015, 'sector': 'FMCG'},
        'SBIN': {'base_price': 785.50, 'volatility': 0.025, 'sector': 'Banking'},
        'BHARTIARTL': {'base_price': 1545.20, 'volatility': 0.018, 'sector': 'Telecom'},
        'KOTAKBANK': {'base_price': 1775.30, 'volatility': 0.02, 'sector': 'Banking'},
        'LT': {'base_price': 3580.40, 'volatility': 0.02, 'sector': 'Infrastructure'},
        'AXISBANK': {'base_price': 1120.90, 'volatility': 0.023, 'sector': 'Banking'},
        'ASIANPAINT': {'base_price': 2890.50, 'volatility': 0.015, 'sector': 'Paints'},
        'MARUTI': {'base_price': 12850.75, 'volatility': 0.022, 'sector': 'Automobile'},
        'BAJFINANCE': {'base_price': 7250.60, 'volatility': 0.025, 'sector': 'Finance'},
        'WIPRO': {'base_price': 565.40, 'volatility': 0.018, 'sector': 'IT'},
        'TECHM': {'base_price': 1685.30, 'volatility': 0.019, 'sector': 'IT'},
        'HCLTECH': {'base_price': 1890.80, 'volatility': 0.017, 'sector': 'IT'},
        'SUNPHARMA': {'base_price': 1745.90, 'volatility': 0.016, 'sector': 'Pharma'},
        'TITAN': {'base_price': 3420.50, 'volatility': 0.02, 'sector': 'Jewellery'}
    }
    
    def __init__(self, seed: int = None):
        """
        Initialize mock data generator.
        
        Args:
            seed: Random seed for reproducible results
        """
        if seed:
            random.seed(seed)
    
    def _calculate_price_movement(self, base_price: float, volatility: float) -> tuple:
        """
        Calculate realistic price movement.
        
        Returns:
            Tuple of (current_price, change, change_percent)
        """
        # Random walk with drift
        change_percent = random.gauss(0, volatility * 100)
        change = base_price * (change_percent / 100)
        current_price = base_price + change
        
        return round(current_price, 2), round(change, 2), round(change_percent, 2)
    
    def get_stock_quote(self, symbol: str) -> Dict:
        """
        Generate mock stock quote data.
        
        Args:
            symbol: Stock symbol (e.g., 'RELIANCE', 'TCS')
        
        Returns:
            Dictionary containing mock stock quote
        """
        symbol_clean = symbol.replace('.NS', '').upper()
        
        if symbol_clean not in self.STOCK_DATA:
            return {
                'error': f'Stock symbol {symbol} not found in mock database',
                'symbol': symbol,
                'available_symbols': list(self.STOCK_DATA.keys())
            }
        
        stock_info = self.STOCK_DATA[symbol_clean]
        base_price = stock_info['base_price']
        volatility = stock_info['volatility']
        
        current_price, change, change_percent = self._calculate_price_movement(base_price, volatility)
        previous_close = base_price
        
        volume = random.randint(1000000, 50000000)
        
        return {
            'symbol': f"{symbol_clean}.NS",
            'name': symbol_clean,
            'price': current_price,
            'previous_close': previous_close,
            'change': change,
            'change_percent': change_percent,
            'volume': volume,
            'open': round(base_price * (1 + random.uniform(-0.01, 0.01)), 2),
            'high': round(current_price * (1 + random.uniform(0, 0.02)), 2),
            'low': round(current_price * (1 - random.uniform(0, 0.02)), 2),
            'sector': stock_info['sector'],
            'currency': 'INR',
            'exchange': 'NSE',
            'timestamp': datetime.now().isoformat(),
            'source': 'Mock Data Generator',
            'note': 'This is simulated data for demonstration purposes'
        }
    
    def get_historical_data(self, symbol: str, days: int = 30) -> Dict:
        """
        Generate mock historical data.
        
        Args:
            symbol: Stock symbol
            days: Number of days of historical data
        
        Returns:
            Dictionary containing historical data
        """
        symbol_clean = symbol.replace('.NS', '').upper()
        
        if symbol_clean not in self.STOCK_DATA:
            return {'error': f'Stock symbol {symbol} not found', 'symbol': symbol}
        
        stock_info = self.STOCK_DATA[symbol_clean]
        base_price = stock_info['base_price']
        volatility = stock_info['volatility']
        
        historical_data = []
        current_price = base_price
        
        for i in range(days, 0, -1):
            date = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d')
            
            # Simulate daily price movement
            open_price = current_price
            change_factor = random.gauss(0, volatility)
            close_price = round(current_price * (1 + change_factor), 2)
            high_price = round(max(open_price, close_price) * (1 + random.uniform(0, 0.015)), 2)
            low_price = round(min(open_price, close_price) * (1 - random.uniform(0, 0.015)), 2)
            volume = random.randint(1000000, 50000000)
            
            historical_data.append({
                'date': date,
                'open': open_price,
                'high': high_price,
                'low': low_price,
                'close': close_price,
                'volume': volume
            })
            
            current_price = close_price
        
        return {
            'symbol': f"{symbol_clean}.NS",
            'period': f'{days} days',
            'data': historical_data,
            'count': len(historical_data),
            'source': 'Mock Data Generator',
            'note': 'This is simulated data for demonstration purposes'
        }
    
    def get_top_gainers_losers(self, count: int = 10) -> Dict:
        """
        Generate mock gainers and losers data.
        
        Args:
            count: Number of stocks in each category
        
        Returns:
            Dictionary with gainers and losers
        """
        all_stocks = []
        
        for symbol in list(self.STOCK_DATA.keys())[:count * 2]:
            quote = self.get_stock_quote(symbol)
            if 'error' not in quote:
                all_stocks.append(quote)
        
        # Sort by change percentage
        all_stocks.sort(key=lambda x: x['change_percent'], reverse=True)
        
        gainers = [s for s in all_stocks if s['change_percent'] > 0][:count]
        losers = [s for s in all_stocks if s['change_percent'] < 0][:count]
        losers.sort(key=lambda x: x['change_percent'])
        
        return {
            'gainers': gainers,
            'losers': losers,
            'timestamp': datetime.now().isoformat(),
            'source': 'Mock Data Generator',
            'note': 'This is simulated data for demonstration purposes'
        }
    
    def get_market_summary(self) -> Dict:
        """
        Generate mock market summary with indices.
        
        Returns:
            Dictionary containing market indices
        """
        nifty_50_base = 22500
        bank_nifty_base = 48200
        
        nifty_change = random.gauss(0, 1.0)
        bank_nifty_change = random.gauss(0, 1.2)
        
        return {
            'NIFTY 50': {
                'value': round(nifty_50_base + (nifty_50_base * nifty_change / 100), 2),
                'change': round(nifty_50_base * nifty_change / 100, 2),
                'change_percent': round(nifty_change, 2),
                'timestamp': datetime.now().isoformat()
            },
            'BANK NIFTY': {
                'value': round(bank_nifty_base + (bank_nifty_base * bank_nifty_change / 100), 2),
                'change': round(bank_nifty_base * bank_nifty_change / 100, 2),
                'change_percent': round(bank_nifty_change, 2),
                'timestamp': datetime.now().isoformat()
            },
            'source': 'Mock Data Generator',
            'note': 'This is simulated data for demonstration purposes'
        }
    
    def get_portfolio_data(self, symbols: List[str]) -> List[Dict]:
        """
        Generate mock portfolio data for multiple symbols.
        
        Args:
            symbols: List of stock symbols
        
        Returns:
            List of stock quotes
        """
        portfolio = []
        for symbol in symbols:
            quote = self.get_stock_quote(symbol)
            if 'error' not in quote:
                portfolio.append(quote)
        
        return portfolio


def demo():
    """Demonstration of mock data generator."""
    print("=" * 80)
    print("Mock NSE Stock Data Generator - Demo")
    print("=" * 80)
    print()
    print("NOTE: This generates realistic simulated data for demonstration purposes.")
    print("      Real API integration available when API keys are configured.")
    print()
    
    mock = MockNSEData(seed=42)  # Use seed for reproducible demo
    
    # Test 1: Get single stock quote
    print("1. RELIANCE Stock Quote:")
    print("-" * 80)
    reliance = mock.get_stock_quote('RELIANCE')
    print(json.dumps(reliance, indent=2))
    print()
    
    # Test 2: Get TCS stock quote
    print("2. TCS Stock Quote:")
    print("-" * 80)
    tcs = mock.get_stock_quote('TCS')
    print(json.dumps(tcs, indent=2))
    print()
    
    # Test 3: Get historical data
    print("3. INFY Historical Data (7 days):")
    print("-" * 80)
    infy_hist = mock.get_historical_data('INFY', days=7)
    print(f"Symbol: {infy_hist['symbol']}")
    print(f"Period: {infy_hist['period']}")
    print(f"Data Points: {infy_hist['count']}")
    print(f"Sample (first 3 days):")
    print(json.dumps(infy_hist['data'][:3], indent=2))
    print()
    
    # Test 4: Get top gainers and losers
    print("4. Top Gainers and Losers (5 each):")
    print("-" * 80)
    gainers_losers = mock.get_top_gainers_losers(count=5)
    print(f"Top Gainers ({len(gainers_losers['gainers'])}):")
    for stock in gainers_losers['gainers']:
        print(f"  {stock['symbol']}: {stock['change_percent']:+.2f}% (₹{stock['price']:.2f})")
    print()
    print(f"Top Losers ({len(gainers_losers['losers'])}):")
    for stock in gainers_losers['losers']:
        print(f"  {stock['symbol']}: {stock['change_percent']:+.2f}% (₹{stock['price']:.2f})")
    print()
    
    # Test 5: Market summary
    print("5. Market Summary:")
    print("-" * 80)
    market = mock.get_market_summary()
    for index_name, index_data in market.items():
        if index_name not in ['source', 'note']:
            print(f"{index_name}: {index_data['value']:.2f} ({index_data['change_percent']:+.2f}%)")
    print()
    
    # Test 6: Portfolio
    print("6. Sample Portfolio:")
    print("-" * 80)
    portfolio_symbols = ['RELIANCE', 'TCS', 'INFY', 'HDFCBANK']
    portfolio = mock.get_portfolio_data(portfolio_symbols)
    total_value = sum(stock['price'] for stock in portfolio)
    print(f"Stocks: {len(portfolio)}")
    for stock in portfolio:
        print(f"  {stock['symbol']}: ₹{stock['price']:.2f} ({stock['change_percent']:+.2f}%)")
    print(f"Total Portfolio Value: ₹{total_value:.2f}")
    print()
    
    print("=" * 80)
    print("Demo Complete!")
    print("=" * 80)
    print()
    print("This mock data generator provides:")
    print("  ✓ Realistic stock prices with volatility")
    print("  ✓ Historical data generation")
    print("  ✓ Market indices (NIFTY, BANK NIFTY)")
    print("  ✓ Gainers/Losers tracking")
    print("  ✓ Portfolio management support")
    print()
    print("Use this for development and demonstration without requiring live APIs.")
    print("=" * 80)


if __name__ == "__main__":
    demo()
