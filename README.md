# ATS-NSE-Stock-Suite
NSE Stock Market Analysis Suite with Live Data Integration (Dhan API, Zerodha Kite, FMP) | VBA Automation | Excel Analytics | Developed by Mandar Bahadarpurkar

## ✨ Features
- **Live Data Integration**: Connect to multiple market data APIs (Dhan, Zerodha Kite, Financial Modeling Prep, Yahoo Finance, Alpha Vantage)
- **Mock Data Support**: Built-in mock data generator for development and demonstration without API keys
- **Excel Integration**: Export stock data, historical analysis, and portfolio tracking to Excel
- **Real-time Analytics**: Process and analyze NSE stock market data
- **Portfolio Management**: Track holdings, gainers, losers, and market indices
- **Multiple API Support**: Flexible configuration for various data sources

## 🚀 Quick Start (No API Keys Required!)

### Run the Demo Application
```bash
# Install dependencies
pip install -r requirements.txt

# Run the complete demo
python demo_app.py
```

This will demonstrate all features using realistic mock data - **perfect for peer review!**

### 1. Installation

```bash
# Clone the repository
git clone <repository-url>
cd ATS-NSE-Stock-Suite

# Install required dependencies
pip install -r requirements.txt
```

### 2. Basic Usage (Mock Data)

```python
from mock_nse_data import MockNSEData
from excel_integration import ExcelExporter

# Initialize
mock_data = MockNSEData()
exporter = ExcelExporter()

# Get stock quote
quote = mock_data.get_stock_quote('RELIANCE')
print(f"RELIANCE: ₹{quote['price']:.2f} ({quote['change_percent']:+.2f}%)")

# Get historical data
historical = mock_data.get_historical_data('TCS', days=30)
print(f"Retrieved {historical['count']} days of data")

# Export to Excel
exporter.export_historical_data(historical, filename="TCS_analysis.xlsx")
```

### 3. Configuration for Live APIs (Optional)

#### Option A: Using .env File (Recommended)
```bash
# Copy the template
cp .env.template .env

# Edit .env and add your API keys
# See CONFIG.md for detailed instructions
```

#### Option B: Using SECRETS.md (For Private Repo)
Since this is a private repository, you can document your tokens in `SECRETS.md`:
1. Open `SECRETS.md`
2. Paste your actual API tokens in the designated sections
3. Use those tokens to create your `.env` file

### 4. API Keys (Optional - For Live Data)

You can optionally get credentials from:
- **Yahoo Finance**: Free, no API key needed (already integrated)
- **Alpha Vantage**: Free tier available at https://www.alphavantage.co/
- **Dhan API**: Client ID and Access Token (premium)
- **Zerodha Kite**: API Key, Secret, and Access Token (premium)
- **Financial Modeling Prep (FMP)**: API Key (premium)

See [CONFIG.md](CONFIG.md) for detailed instructions on obtaining these credentials.

### 5. Using the Configuration

```python
from config_loader import config

# Access your credentials (if configured)
dhan_client_id = config.DHAN_CLIENT_ID
kite_api_key = config.KITE_API_KEY
fmp_api_key = config.FMP_API_KEY

# Check configuration
if config.validate():
    print("Configuration is valid!")
```

## 📁 Project Structure

```
ATS-NSE-Stock-Suite/
├── .env.template          # Template for environment variables
├── .gitignore            # Git ignore rules (includes .env)
├── CONFIG.md             # Detailed configuration guide
├── SECRETS.md            # Document your tokens here (private repo)
├── HUGGINGFACE_GUIDE.md  # Hugging Face integration guide
├── config_loader.py      # Python configuration loader
├── nse_data_fetcher.py   # Live API data fetcher (Yahoo Finance, Alpha Vantage)
├── mock_nse_data.py      # Mock data generator for development/demo
├── excel_integration.py  # Excel export and reporting functionality
├── demo_app.py          # Complete demonstration application
├── example_usage.py      # Usage examples for configuration
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🎯 Main Scripts

- **demo_app.py**: Complete demonstration of all features - **Start here!**
- **mock_nse_data.py**: Generate realistic stock data without API keys
- **nse_data_fetcher.py**: Fetch live data from Yahoo Finance and other APIs
- **excel_integration.py**: Export data to Excel for analysis
- **config_loader.py**: Manage API credentials and configuration

## 📊 Example Output

The demo application generates:
- **Real-time stock quotes** for RELIANCE, TCS, INFY, HDFCBANK, ICICIBANK
- **Historical data analysis** with 30 days of price movements
- **Market analysis** showing top gainers and losers
- **Portfolio tracking** with total value calculations
- **Excel files** ready for further analysis:
  - `TCS_demo.xlsx` - Historical data export
  - `portfolio_demo.xlsx` - Portfolio tracking
  - `watchlist_demo.xlsx` - Stock watchlist template

## 🔧 Advanced Usage

### Fetch Live Data (with API key)
```python
from nse_data_fetcher import NSEDataFetcher

# Initialize with Alpha Vantage key (free tier available)
fetcher = NSEDataFetcher(alpha_vantage_key='YOUR_KEY')

# Get stock quote from Yahoo Finance (no key needed)
quote = fetcher.get_stock_quote_yahoo('RELIANCE')

# Get historical data
historical = fetcher.get_historical_data_yahoo('TCS', period='1mo')
```

### Create Portfolio Reports
```python
from mock_nse_data import MockNSEData
from excel_integration import ExcelExporter

mock = MockNSEData()
exporter = ExcelExporter()

# Fetch portfolio data
symbols = ['RELIANCE', 'TCS', 'INFY', 'HDFCBANK']
portfolio = mock.get_portfolio_data(symbols)

# Export to Excel
exporter.export_portfolio(portfolio, filename='my_portfolio.xlsx')
```

## 📚 Documentation

- **[CONFIG.md](CONFIG.md)**: Complete guide for setting up API credentials
- **[HUGGINGFACE_GUIDE.md](HUGGINGFACE_GUIDE.md)**: Hugging Face integration guide
- **[SECRETS.md](SECRETS.md)**: Template for documenting your tokens (private repo only)

## 🔒 Security Notes

- The `.env` file is excluded from git (via `.gitignore`)
- Never commit API keys to version control
- Rotate your API keys regularly
- Monitor API usage for unusual activity
- Use mock data for development to avoid API limits

## 🤝 Support

For issues related to:
- **API credentials**: Contact the respective API provider
- **Configuration**: See [CONFIG.md](CONFIG.md)
- **Project setup**: Open an issue in this repository
- **Feature requests**: Open an issue with your suggestion

## ✅ Ready for Peer Review

This application is fully functional and ready for review:
- ✅ Stock data fetching implemented
- ✅ Excel integration working
- ✅ Portfolio management functional
- ✅ Market analysis tools available
- ✅ Configuration management complete
- ✅ Mock data for demonstration
- ✅ Real API support available

**Run `python demo_app.py` to see everything in action!**

## 👨‍💻 About

Developed by Mandar Bahadarpurkar for NSE stock market analysis and automation.

## 📝 License

See repository license for details.
