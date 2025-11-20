"""
Excel Integration for NSE Stock Data
=====================================

This module provides functionality to export NSE stock data to Excel format
and integrate with Excel-based analytics tools.

Features:
- Export stock quotes to Excel
- Create formatted Excel reports
- Historical data export
- Portfolio tracking sheets

Author: Mandar Bahadarpurkar
"""

import pandas as pd
from datetime import datetime
from typing import Dict, List, Optional
import json


class ExcelExporter:
    """Export NSE stock data to Excel format."""
    
    def __init__(self, output_dir: str = "."):
        """
        Initialize Excel Exporter.
        
        Args:
            output_dir: Directory to save Excel files
        """
        self.output_dir = output_dir
    
    def export_stock_quote(self, quote_data: Dict, filename: Optional[str] = None) -> str:
        """
        Export stock quote to Excel file.
        
        Args:
            quote_data: Stock quote dictionary
            filename: Optional filename (auto-generated if not provided)
        
        Returns:
            Path to created Excel file
        """
        if not filename:
            symbol = quote_data.get('symbol', 'stock').replace('.NS', '')
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"{symbol}_quote_{timestamp}.xlsx"
        
        filepath = f"{self.output_dir}/{filename}"
        
        # Convert to DataFrame
        df = pd.DataFrame([quote_data])
        
        # Export to Excel
        with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Quote', index=False)
        
        return filepath
    
    def export_historical_data(self, historical_data: Dict, filename: Optional[str] = None) -> str:
        """
        Export historical stock data to Excel file.
        
        Args:
            historical_data: Historical data dictionary with 'data' key containing list of records
            filename: Optional filename (auto-generated if not provided)
        
        Returns:
            Path to created Excel file
        """
        if not filename:
            symbol = historical_data.get('symbol', 'stock').replace('.NS', '')
            period = historical_data.get('period', '').replace(' ', '_')
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"{symbol}_historical_{period}_{timestamp}.xlsx"
        
        filepath = f"{self.output_dir}/{filename}"
        
        # Convert to DataFrame
        if 'data' in historical_data and historical_data['data']:
            df = pd.DataFrame(historical_data['data'])
            
            # Export to Excel with formatting
            with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Historical Data', index=False)
                
                # Add metadata sheet
                metadata_df = pd.DataFrame([{
                    'Symbol': historical_data.get('symbol'),
                    'Period': historical_data.get('period'),
                    'Source': historical_data.get('source'),
                    'Data Points': historical_data.get('count'),
                    'Export Date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }])
                metadata_df.to_excel(writer, sheet_name='Metadata', index=False)
        
        return filepath
    
    def export_portfolio(self, portfolio_data: List[Dict], filename: Optional[str] = None) -> str:
        """
        Export portfolio data to Excel file.
        
        Args:
            portfolio_data: List of stock quote dictionaries
            filename: Optional filename (auto-generated if not provided)
        
        Returns:
            Path to created Excel file
        """
        if not filename:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"portfolio_{timestamp}.xlsx"
        
        filepath = f"{self.output_dir}/{filename}"
        
        # Convert to DataFrame
        df = pd.DataFrame(portfolio_data)
        
        # Calculate portfolio metrics if possible
        if 'price' in df.columns and 'volume' in df.columns:
            total_value = (df['price'] * df['volume']).sum() if 'volume' in df.columns else 0
            
            summary_df = pd.DataFrame([{
                'Total Stocks': len(df),
                'Portfolio Value': total_value,
                'Generated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }])
        
        # Export to Excel
        with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Holdings', index=False)
            if 'price' in df.columns and 'volume' in df.columns:
                summary_df.to_excel(writer, sheet_name='Summary', index=False)
        
        return filepath
    
    def export_gainers_losers(self, data: Dict, filename: Optional[str] = None) -> str:
        """
        Export top gainers and losers to Excel file.
        
        Args:
            data: Dictionary with 'gainers' and 'losers' keys
            filename: Optional filename (auto-generated if not provided)
        
        Returns:
            Path to created Excel file
        """
        if not filename:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"gainers_losers_{timestamp}.xlsx"
        
        filepath = f"{self.output_dir}/{filename}"
        
        # Export to Excel with multiple sheets
        with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
            if 'gainers' in data and data['gainers']:
                gainers_df = pd.DataFrame(data['gainers'])
                gainers_df.to_excel(writer, sheet_name='Top Gainers', index=False)
            
            if 'losers' in data and data['losers']:
                losers_df = pd.DataFrame(data['losers'])
                losers_df.to_excel(writer, sheet_name='Top Losers', index=False)
        
        return filepath
    
    def create_watchlist_template(self, filename: Optional[str] = None) -> str:
        """
        Create an Excel template for stock watchlist.
        
        Args:
            filename: Optional filename
        
        Returns:
            Path to created Excel file
        """
        if not filename:
            filename = "watchlist_template.xlsx"
        
        filepath = f"{self.output_dir}/{filename}"
        
        # Create template DataFrame
        template_data = {
            'Symbol': ['RELIANCE', 'TCS', 'INFY'],
            'Target Price': [2800, 4000, 1600],
            'Stop Loss': [2400, 3500, 1400],
            'Quantity': [10, 5, 20],
            'Notes': ['Sample entry', 'Sample entry', 'Sample entry']
        }
        
        df = pd.DataFrame(template_data)
        
        # Export to Excel
        with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Watchlist', index=False)
            
            # Add instructions sheet
            instructions = pd.DataFrame([{
                'Instructions': 'Add your stocks to track in the Watchlist sheet',
                'Symbol Format': 'Use stock symbols without .NS suffix (e.g., RELIANCE, TCS)',
                'Usage': 'Update Target Price and Stop Loss as per your strategy'
            }])
            instructions.to_excel(writer, sheet_name='Instructions', index=False)
        
        return filepath


def demo():
    """Demonstration of Excel export functionality."""
    print("=" * 80)
    print("Excel Integration Demo")
    print("=" * 80)
    print()
    
    # Try to import the data fetcher
    try:
        from nse_data_fetcher import NSEDataFetcher
        
        print("Initializing NSE Data Fetcher and Excel Exporter...")
        fetcher = NSEDataFetcher()
        exporter = ExcelExporter(output_dir=".")
        
        # Test 1: Export stock quote
        print("\n1. Exporting RELIANCE stock quote to Excel...")
        quote = fetcher.get_stock_quote_yahoo('RELIANCE')
        if 'error' not in quote:
            filepath = exporter.export_stock_quote(quote)
            print(f"✓ Exported to: {filepath}")
        else:
            print(f"✗ Error: {quote['error']}")
        
        # Test 2: Export historical data
        print("\n2. Exporting TCS historical data to Excel...")
        historical = fetcher.get_historical_data_yahoo('TCS', period='1mo')
        if 'error' not in historical:
            filepath = exporter.export_historical_data(historical)
            print(f"✓ Exported to: {filepath}")
        else:
            print(f"✗ Error: {historical['error']}")
        
        # Test 3: Create watchlist template
        print("\n3. Creating watchlist template...")
        filepath = exporter.create_watchlist_template()
        print(f"✓ Created: {filepath}")
        
        print("\n" + "=" * 80)
        print("Excel export demo completed!")
        print("Check the current directory for generated Excel files.")
        print("=" * 80)
        
    except ImportError:
        print("Note: This demo requires nse_data_fetcher.py")
        print("Run 'python nse_data_fetcher.py' first to test data fetching.")
        print()
        
        # Create sample exporter without data fetcher
        print("Creating sample Excel template...")
        exporter = ExcelExporter(output_dir=".")
        filepath = exporter.create_watchlist_template()
        print(f"✓ Created watchlist template: {filepath}")
        print()
        print("Install required packages:")
        print("  pip install pandas openpyxl")


if __name__ == "__main__":
    demo()
