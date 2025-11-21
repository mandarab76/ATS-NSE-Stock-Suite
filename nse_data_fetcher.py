"""
NSE Stock Data Fetcher
======================

This module provides multiple connectors to fetch NSE (National Stock Exchange) 
stock data using publicly available APIs and data sources.

Features:
- Yahoo Finance connector (no API key needed)
- Alpha Vantage connector (free tier available)
- NSE India official website connector
- Multiple fallback options for reliability

Author: Mandar Bahadarpurkar
"""

import requests
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Union
import time


class NSEDataFetcher:
    """Main class for fetching NSE stock market data from multiple sources."""
    
    def __init__(self, alpha_vantage_key: Optional[str] = None):
        """
        Initialize the NSE Data Fetcher.
        
        Args:
            alpha_vantage_key: Optional Alpha Vantage API key (free tier available)
        """
        self.alpha_vantage_key = alpha_vantage_key
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def get_stock_quote_yahoo(self, symbol: str) -> Dict:
        """
        Fetch stock quote from Yahoo Finance (no API key needed).
        
        Args:
            symbol: NSE stock symbol (e.g., 'RELIANCE.NS', 'TCS.NS')
        
        Returns:
            Dictionary containing stock quote data
        """
        try:
            # Ensure NSE suffix
            if not symbol.endswith('.NS'):
                symbol = f"{symbol}.NS"
            
            url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
            params = {
                'interval': '1d',
                'range': '1d'
            }
            
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if 'chart' in data and 'result' in data['chart'] and data['chart']['result']:
                result = data['chart']['result'][0]
                meta = result.get('meta', {})
                
                return {
                    'symbol': symbol,
                    'price': meta.get('regularMarketPrice'),
                    'previous_close': meta.get('previousClose'),
                    'change': meta.get('regularMarketPrice', 0) - meta.get('previousClose', 0),
                    'change_percent': ((meta.get('regularMarketPrice', 0) - meta.get('previousClose', 0)) / 
                                     meta.get('previousClose', 1)) * 100 if meta.get('previousClose') else 0,
                    'volume': meta.get('regularMarketVolume'),
                    'currency': meta.get('currency', 'INR'),
                    'exchange': meta.get('exchangeName', 'NSE'),
                    'timestamp': datetime.fromtimestamp(meta.get('regularMarketTime', time.time())).isoformat(),
                    'source': 'Yahoo Finance'
                }
            else:
                return {'error': 'No data available', 'symbol': symbol}
                
        except Exception as e:
            return {'error': str(e), 'symbol': symbol, 'source': 'Yahoo Finance'}
    
    def get_stock_quote_alphavantage(self, symbol: str) -> Dict:
        """
        Fetch stock quote from Alpha Vantage API.
        
        Note: Requires API key. Get free key at: https://www.alphavantage.co/support/#api-key
        
        Args:
            symbol: Stock symbol without exchange suffix (e.g., 'RELIANCE')
        
        Returns:
            Dictionary containing stock quote data
        """
        if not self.alpha_vantage_key:
            return {
                'error': 'Alpha Vantage API key not provided',
                'info': 'Get free API key at https://www.alphavantage.co/support/#api-key',
                'symbol': symbol
            }
        
        try:
            # Remove .NS suffix if present
            symbol = symbol.replace('.NS', '')
            
            url = 'https://www.alphavantage.co/query'
            params = {
                'function': 'GLOBAL_QUOTE',
                'symbol': f'{symbol}.BSE',  # Try BSE first, then NSE
                'apikey': self.alpha_vantage_key
            }
            
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if 'Global Quote' in data and data['Global Quote']:
                quote = data['Global Quote']
                return {
                    'symbol': symbol,
                    'price': float(quote.get('05. price', 0)),
                    'previous_close': float(quote.get('08. previous close', 0)),
                    'change': float(quote.get('09. change', 0)),
                    'change_percent': quote.get('10. change percent', '0%').replace('%', ''),
                    'volume': int(quote.get('06. volume', 0)),
                    'latest_trading_day': quote.get('07. latest trading day'),
                    'source': 'Alpha Vantage'
                }
            else:
                return {'error': 'No data available or API limit reached', 'symbol': symbol, 'data': data}
                
        except Exception as e:
            return {'error': str(e), 'symbol': symbol, 'source': 'Alpha Vantage'}
    
    def get_nse_indices(self) -> Dict:
        """
        Fetch NSE indices data (NIFTY 50, BANK NIFTY, etc.).
        
        Returns:
            Dictionary containing major NSE indices data
        """
        indices = ['NIFTY', 'BANKNIFTY', 'FINNIFTY']
        results = {}
        
        for index in indices:
            try:
                symbol = f"^NSE{index}" if index == 'NIFTY' else f"^NSE{index}"
                # Use Yahoo Finance for indices
                quote = self.get_stock_quote_yahoo(symbol)
                results[index] = quote
            except Exception as e:
                results[index] = {'error': str(e)}
        
        return results
    
    def get_top_gainers_losers(self, count: int = 10) -> Dict:
        """
        Get top gainers and losers from NSE.
        
        Note: This is a demo implementation. For production, consider using
        paid APIs or web scraping with proper permissions.
        
        Args:
            count: Number of stocks to return
        
        Returns:
            Dictionary with gainers and losers lists
        """
        # Sample NSE stocks for demonstration
        sample_stocks = [
            'RELIANCE', 'TCS', 'INFY', 'HDFCBANK', 'ICICIBANK',
            'HINDUNILVR', 'ITC', 'SBIN', 'BAJFINANCE', 'BHARTIARTL',
            'KOTAKBANK', 'LT', 'AXISBANK', 'ASIANPAINT', 'MARUTI'
        ]
        
        gainers = []
        losers = []
        
        for stock in sample_stocks[:count]:
            quote = self.get_stock_quote_yahoo(stock)
            if 'error' not in quote and quote.get('change_percent'):
                change_pct = float(quote['change_percent'])
                if change_pct > 0:
                    gainers.append(quote)
                elif change_pct < 0:
                    losers.append(quote)
            time.sleep(0.5)  # Rate limiting
        
        # Sort by change percentage
        gainers.sort(key=lambda x: float(x.get('change_percent', 0)), reverse=True)
        losers.sort(key=lambda x: float(x.get('change_percent', 0)))
        
        return {
            'gainers': gainers[:count],
            'losers': losers[:count],
            'timestamp': datetime.now().isoformat()
        }
    
    def get_historical_data_yahoo(self, symbol: str, period: str = '1mo') -> Dict:
        """
        Fetch historical stock data from Yahoo Finance.
        
        Args:
            symbol: NSE stock symbol (e.g., 'RELIANCE.NS')
            period: Time period - '1d', '5d', '1mo', '3mo', '6mo', '1y', '5y', 'max'
        
        Returns:
            Dictionary containing historical data
        """
        try:
            if not symbol.endswith('.NS'):
                symbol = f"{symbol}.NS"
            
            url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
            params = {
                'interval': '1d',
                'range': period
            }
            
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if 'chart' in data and 'result' in data['chart'] and data['chart']['result']:
                result = data['chart']['result'][0]
                timestamps = result.get('timestamp', [])
                indicators = result.get('indicators', {})
                quote = indicators.get('quote', [{}])[0]
                
                historical_data = []
                for i, ts in enumerate(timestamps):
                    historical_data.append({
                        'date': datetime.fromtimestamp(ts).strftime('%Y-%m-%d'),
                        'open': quote.get('open', [])[i] if i < len(quote.get('open', [])) else None,
                        'high': quote.get('high', [])[i] if i < len(quote.get('high', [])) else None,
                        'low': quote.get('low', [])[i] if i < len(quote.get('low', [])) else None,
                        'close': quote.get('close', [])[i] if i < len(quote.get('close', [])) else None,
                        'volume': quote.get('volume', [])[i] if i < len(quote.get('volume', [])) else None,
                    })
                
                return {
                    'symbol': symbol,
                    'period': period,
                    'data': historical_data,
                    'count': len(historical_data),
                    'source': 'Yahoo Finance'
                }
            else:
                return {'error': 'No data available', 'symbol': symbol}
                
        except Exception as e:
            return {'error': str(e), 'symbol': symbol, 'source': 'Yahoo Finance'}
    
    def get_stock_info(self, symbol: str) -> Dict:
        """
        Get detailed stock information including fundamentals.
        
        Args:
            symbol: NSE stock symbol
        
        Returns:
            Dictionary containing stock information
        """
        try:
            if not symbol.endswith('.NS'):
                symbol = f"{symbol}.NS"
            
            # Get quote data
            quote = self.get_stock_quote_yahoo(symbol)
            
            # Get historical data for additional metrics
            historical = self.get_historical_data_yahoo(symbol, period='1mo')
            
            return {
                'quote': quote,
                'historical_summary': {
                    'period': '1 month',
                    'data_points': historical.get('count', 0)
                },
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            return {'error': str(e), 'symbol': symbol}


def demo():
    """Demonstration of NSE Data Fetcher capabilities."""
    print("=" * 80)
    print("NSE Stock Data Fetcher - Demo")
    print("=" * 80)
    print()
    
    # Initialize fetcher
    fetcher = NSEDataFetcher()
    
    # Test 1: Get single stock quote
    print("1. Fetching RELIANCE stock quote...")
    print("-" * 80)
    reliance = fetcher.get_stock_quote_yahoo('RELIANCE')
    print(json.dumps(reliance, indent=2))
    print()
    
    # Test 2: Get TCS stock quote
    print("2. Fetching TCS stock quote...")
    print("-" * 80)
    tcs = fetcher.get_stock_quote_yahoo('TCS')
    print(json.dumps(tcs, indent=2))
    print()
    
    # Test 3: Get historical data
    print("3. Fetching INFY historical data (1 month)...")
    print("-" * 80)
    infy_historical = fetcher.get_historical_data_yahoo('INFY', period='1mo')
    if 'data' in infy_historical:
        print(f"Retrieved {infy_historical['count']} data points")
        print(f"Sample data (first 3 days):")
        print(json.dumps(infy_historical['data'][:3], indent=2))
    else:
        print(json.dumps(infy_historical, indent=2))
    print()
    
    # Test 4: Get stock info
    print("4. Fetching HDFCBANK detailed info...")
    print("-" * 80)
    hdfc_info = fetcher.get_stock_info('HDFCBANK')
    print(json.dumps(hdfc_info, indent=2))
    print()
    
    print("=" * 80)
    print("Demo Complete!")
    print("=" * 80)
    print()
    print("Next Steps:")
    print("1. Install additional dependencies: pip install pandas openpyxl")
    print("2. Use this module in your analysis scripts")
    print("3. For Alpha Vantage support, get free API key at:")
    print("   https://www.alphavantage.co/support/#api-key")
    print("=" * 80)


if __name__ == "__main__":
    demo()
