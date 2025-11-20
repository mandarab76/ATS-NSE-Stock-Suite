"""
Example Usage of ATS-NSE-Stock-Suite Configuration

This script demonstrates how to use the configuration loader
to access API credentials and connect to various services.
"""

from config_loader import config
import sys


def check_configuration():
    """Check if configuration is properly set up."""
    print("=" * 70)
    print("ATS-NSE-Stock-Suite - Configuration Check")
    print("=" * 70)
    print()
    
    # Display configuration status (without exposing secrets)
    print("Configuration Status:")
    print("-" * 70)
    print(f"Dhan API:        {'✓ Configured' if config.DHAN_CLIENT_ID else '✗ Not configured'}")
    print(f"Zerodha Kite:    {'✓ Configured' if config.KITE_API_KEY else '✗ Not configured'}")
    print(f"FMP API:         {'✓ Configured' if config.FMP_API_KEY else '✗ Not configured'}")
    print(f"Hugging Face:    {'✓ Configured' if config.HUGGINGFACE_TOKEN else '✗ Not configured'}")
    print(f"Database:        {'✓ Configured' if config.DATABASE_URL else '✗ Not configured'}")
    print()
    print(f"Debug Mode:      {config.DEBUG_MODE}")
    print(f"Log Level:       {config.LOG_LEVEL}")
    print("-" * 70)
    print()


def example_dhan_setup():
    """Example of setting up Dhan API connection."""
    print("Dhan API Setup Example:")
    print("-" * 70)
    
    if not config.DHAN_CLIENT_ID or not config.DHAN_ACCESS_TOKEN:
        print("⚠ Dhan API credentials not configured!")
        print("Add DHAN_CLIENT_ID and DHAN_ACCESS_TOKEN to your .env file")
        return
    
    print("✓ Dhan credentials found")
    print()
    print("Example code to use Dhan API:")
    print("""
    from dhanhq import dhanhq
    
    dhan = dhanhq(
        client_id=config.DHAN_CLIENT_ID,
        access_token=config.DHAN_ACCESS_TOKEN
    )
    
    # Get holdings
    holdings = dhan.get_holdings()
    print(holdings)
    """)
    print()


def example_kite_setup():
    """Example of setting up Zerodha Kite API connection."""
    print("Zerodha Kite API Setup Example:")
    print("-" * 70)
    
    if not config.KITE_API_KEY:
        print("⚠ Kite API credentials not configured!")
        print("Add KITE_API_KEY, KITE_API_SECRET, and KITE_ACCESS_TOKEN to your .env file")
        return
    
    print("✓ Kite credentials found")
    print()
    print("Example code to use Kite API:")
    print("""
    from kiteconnect import KiteConnect
    
    kite = KiteConnect(api_key=config.KITE_API_KEY)
    
    # Set access token (after login flow)
    kite.set_access_token(config.KITE_ACCESS_TOKEN)
    
    # Get positions
    positions = kite.positions()
    print(positions)
    """)
    print()


def example_fmp_setup():
    """Example of setting up FMP API connection."""
    print("Financial Modeling Prep API Setup Example:")
    print("-" * 70)
    
    if not config.FMP_API_KEY:
        print("⚠ FMP API key not configured!")
        print("Add FMP_API_KEY to your .env file")
        return
    
    print("✓ FMP API key found")
    print()
    print("Example code to use FMP API:")
    print("""
    import requests
    
    # Example: Get stock quote
    symbol = "AAPL"
    url = f"https://financialmodelingprep.com/api/v3/quote/{symbol}"
    params = {"apikey": config.FMP_API_KEY}
    
    response = requests.get(url, params=params)
    data = response.json()
    print(data)
    """)
    print()


def example_huggingface_setup():
    """Example of setting up Hugging Face integration."""
    print("Hugging Face API Setup Example:")
    print("-" * 70)
    
    if not config.HUGGINGFACE_TOKEN:
        print("⚠ Hugging Face token not configured!")
        print("Add HUGGINGFACE_TOKEN to your .env file")
        return
    
    print("✓ Hugging Face token found")
    print()
    print("Example code to use Hugging Face Hub:")
    print("""
    from huggingface_hub import HfApi, HfFolder
    
    # Save token
    HfFolder.save_token(config.HUGGINGFACE_TOKEN)
    
    # Initialize API
    api = HfApi()
    
    # List your models
    models = api.list_models(author="your-username")
    for model in models:
        print(model.modelId)
    
    # Access a space
    if config.HUGGINGFACE_SPACE_URL:
        print(f"Your space: {config.HUGGINGFACE_SPACE_URL}")
    """)
    print()


def main():
    """Main function to run all examples."""
    print()
    
    # Check configuration
    check_configuration()
    
    # Show setup examples for each API
    example_dhan_setup()
    example_kite_setup()
    example_fmp_setup()
    example_huggingface_setup()
    
    # Final instructions
    print("=" * 70)
    print("Next Steps:")
    print("=" * 70)
    print("1. Configure missing credentials in your .env file")
    print("2. Install required API client libraries:")
    print("   pip install dhanhq kiteconnect fmpsdk huggingface-hub requests")
    print("3. Use the example code above to integrate with each API")
    print("4. Check CONFIG.md for detailed setup instructions")
    print("=" * 70)
    print()


if __name__ == "__main__":
    main()
