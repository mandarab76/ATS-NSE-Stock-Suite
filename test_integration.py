"""
Integration Test for ATS-NSE-Stock-Suite
=========================================

This script tests all major components to ensure they work together correctly.
Run this before deployment or peer review to verify everything is functional.

Author: Mandar Bahadarpurkar
"""

import sys
from datetime import datetime


def test_imports():
    """Test that all modules can be imported."""
    print("Testing imports...")
    try:
        from config_loader import config
        from mock_nse_data import MockNSEData
        from excel_integration import ExcelExporter
        from nse_data_fetcher import NSEDataFetcher
        print("✓ All modules imported successfully")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False


def test_mock_data():
    """Test mock data generation."""
    print("\nTesting mock data generator...")
    try:
        from mock_nse_data import MockNSEData
        mock = MockNSEData(seed=42)
        
        # Test stock quote
        quote = mock.get_stock_quote('RELIANCE')
        assert 'price' in quote, "Quote missing price"
        assert 'symbol' in quote, "Quote missing symbol"
        assert quote['symbol'] == 'RELIANCE.NS', "Incorrect symbol format"
        
        # Test historical data
        historical = mock.get_historical_data('TCS', days=7)
        assert historical['count'] == 7, "Incorrect number of historical days"
        assert len(historical['data']) == 7, "Incorrect historical data length"
        
        # Test market summary
        market = mock.get_market_summary()
        assert 'NIFTY 50' in market, "Missing NIFTY 50"
        assert 'BANK NIFTY' in market, "Missing BANK NIFTY"
        
        # Test gainers/losers
        gl = mock.get_top_gainers_losers(count=3)
        assert 'gainers' in gl, "Missing gainers"
        assert 'losers' in gl, "Missing losers"
        
        print("✓ Mock data generator working correctly")
        return True
    except Exception as e:
        print(f"✗ Mock data error: {e}")
        return False


def test_excel_integration():
    """Test Excel export functionality."""
    print("\nTesting Excel integration...")
    try:
        from mock_nse_data import MockNSEData
        from excel_integration import ExcelExporter
        import os
        
        mock = MockNSEData(seed=42)
        exporter = ExcelExporter(output_dir="/tmp")
        
        # Test quote export
        quote = mock.get_stock_quote('TCS')
        filepath = exporter.export_stock_quote(quote, filename="test_quote.xlsx")
        assert os.path.exists(filepath), "Quote Excel file not created"
        os.remove(filepath)
        
        # Test historical export
        historical = mock.get_historical_data('INFY', days=5)
        filepath = exporter.export_historical_data(historical, filename="test_historical.xlsx")
        assert os.path.exists(filepath), "Historical Excel file not created"
        os.remove(filepath)
        
        # Test portfolio export
        portfolio = mock.get_portfolio_data(['RELIANCE', 'TCS'])
        filepath = exporter.export_portfolio(portfolio, filename="test_portfolio.xlsx")
        assert os.path.exists(filepath), "Portfolio Excel file not created"
        os.remove(filepath)
        
        # Test template creation
        filepath = exporter.create_watchlist_template(filename="test_watchlist.xlsx")
        assert os.path.exists(filepath), "Watchlist template not created"
        os.remove(filepath)
        
        print("✓ Excel integration working correctly")
        return True
    except Exception as e:
        print(f"✗ Excel integration error: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_config_loader():
    """Test configuration loader."""
    print("\nTesting configuration loader...")
    try:
        from config_loader import config
        
        # Test that config object exists
        assert config is not None, "Config object is None"
        
        # Test that validation works (should pass even without keys)
        config.validate()
        
        # Test config attributes
        assert hasattr(config, 'DHAN_CLIENT_ID'), "Missing DHAN_CLIENT_ID attribute"
        assert hasattr(config, 'KITE_API_KEY'), "Missing KITE_API_KEY attribute"
        assert hasattr(config, 'FMP_API_KEY'), "Missing FMP_API_KEY attribute"
        assert hasattr(config, 'DEBUG_MODE'), "Missing DEBUG_MODE attribute"
        
        # Test __repr__ doesn't expose secrets
        config_str = str(config)
        assert 'Not set' in config_str or '***' in config_str, "Config repr issue"
        
        print("✓ Configuration loader working correctly")
        return True
    except Exception as e:
        print(f"✗ Configuration error: {e}")
        return False


def test_data_fetcher():
    """Test data fetcher module (structure only, not live API)."""
    print("\nTesting data fetcher module...")
    try:
        from nse_data_fetcher import NSEDataFetcher
        
        # Test initialization
        fetcher = NSEDataFetcher()
        assert fetcher is not None, "Fetcher not initialized"
        
        # Test with Alpha Vantage key
        fetcher_with_key = NSEDataFetcher(alpha_vantage_key='test_key')
        assert fetcher_with_key.alpha_vantage_key == 'test_key', "API key not set"
        
        print("✓ Data fetcher module structure correct")
        return True
    except Exception as e:
        print(f"✗ Data fetcher error: {e}")
        return False


def test_data_accuracy():
    """Test that generated data is realistic."""
    print("\nTesting data accuracy and realism...")
    try:
        from mock_nse_data import MockNSEData
        mock = MockNSEData(seed=42)
        
        # Test price ranges are reasonable
        for symbol in ['RELIANCE', 'TCS', 'INFY']:
            quote = mock.get_stock_quote(symbol)
            assert quote['price'] > 0, f"{symbol} price not positive"
            assert quote['volume'] > 0, f"{symbol} volume not positive"
            assert abs(quote['change_percent']) < 20, f"{symbol} change too large"
        
        # Test historical data consistency
        historical = mock.get_historical_data('TCS', days=10)
        for day in historical['data']:
            assert day['high'] >= day['low'], "High < Low in historical data"
            assert day['high'] >= day['open'], "High < Open in historical data"
            assert day['high'] >= day['close'], "High < Close in historical data"
            assert day['low'] <= day['open'], "Low > Open in historical data"
            assert day['low'] <= day['close'], "Low > Close in historical data"
        
        print("✓ Generated data is accurate and realistic")
        return True
    except Exception as e:
        print(f"✗ Data accuracy error: {e}")
        return False


def run_all_tests():
    """Run all integration tests."""
    print("=" * 80)
    print("ATS-NSE-Stock-Suite - Integration Tests")
    print("=" * 80)
    print(f"Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    tests = [
        test_imports,
        test_config_loader,
        test_mock_data,
        test_data_fetcher,
        test_excel_integration,
        test_data_accuracy,
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"✗ Test failed with exception: {e}")
            results.append(False)
    
    # Summary
    print("\n" + "=" * 80)
    print("Test Summary")
    print("=" * 80)
    passed = sum(results)
    total = len(results)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("\n🎉 All tests passed! Application is ready for peer review.")
        print("=" * 80)
        return 0
    else:
        print(f"\n⚠ {total - passed} test(s) failed. Please review errors above.")
        print("=" * 80)
        return 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
