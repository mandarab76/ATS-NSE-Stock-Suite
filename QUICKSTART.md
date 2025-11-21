# Quick Start Guide - ATS-NSE-Stock-Suite

Get started with the NSE Stock Market Analysis Suite in 5 minutes!

## 🚀 Fastest Way to Get Started

### Step 1: Install Dependencies (30 seconds)
```bash
pip install -r requirements.txt
```

### Step 2: Run the Demo (1 minute)
```bash
python demo_app.py
```

That's it! The demo will show you:
- ✓ Real-time stock quotes for major NSE stocks
- ✓ Historical price data and analysis
- ✓ Portfolio tracking with value calculations
- ✓ Top gainers and losers in the market
- ✓ Market indices (NIFTY 50, BANK NIFTY)
- ✓ Excel exports ready for further analysis

## 📊 What You'll See

The demo application demonstrates the complete functionality:

```
Stock Quotes:
  RELIANCE.NS  | ₹2,642.86 | ▼ -0.29% | Volume: 19,456,905
  TCS.NS       | ₹3,840.76 | ▼ -0.26% | Volume: 37,598,928
  INFY.NS      | ₹1,586.91 | ▲ +0.42% | Volume: 2,780,798

Historical Data:
  ✓ 30 days of OHLC data
  ✓ Volume analysis
  ✓ Exported to Excel

Portfolio:
  5 stocks tracked
  Total value: ₹569,008.20
  Exported to Excel
```

## 🎯 Try It Yourself

### Get a Single Stock Quote
```python
from mock_nse_data import MockNSEData

mock = MockNSEData()
quote = mock.get_stock_quote('RELIANCE')

print(f"Symbol: {quote['symbol']}")
print(f"Price: ₹{quote['price']:.2f}")
print(f"Change: {quote['change_percent']:+.2f}%")
```

### Get Historical Data
```python
from mock_nse_data import MockNSEData

mock = MockNSEData()
historical = mock.get_historical_data('TCS', days=30)

print(f"Retrieved {historical['count']} days of data")
for day in historical['data'][-5:]:  # Last 5 days
    print(f"{day['date']}: ₹{day['close']:.2f}")
```

### Export to Excel
```python
from mock_nse_data import MockNSEData
from excel_integration import ExcelExporter

mock = MockNSEData()
exporter = ExcelExporter()

# Get data
historical = mock.get_historical_data('INFY', days=30)

# Export to Excel
filepath = exporter.export_historical_data(historical)
print(f"Exported to: {filepath}")
```

### Track Your Portfolio
```python
from mock_nse_data import MockNSEData
from excel_integration import ExcelExporter

mock = MockNSEData()
exporter = ExcelExporter()

# Define your portfolio
symbols = ['RELIANCE', 'TCS', 'INFY', 'HDFCBANK']
portfolio = mock.get_portfolio_data(symbols)

# Export to Excel
filepath = exporter.export_portfolio(portfolio)
print(f"Portfolio exported to: {filepath}")
```

## 🌐 Use Live APIs (Optional)

The system works perfectly with mock data, but you can also connect to live APIs:

### Yahoo Finance (Free, No Key Needed)
```python
from nse_data_fetcher import NSEDataFetcher

fetcher = NSEDataFetcher()
quote = fetcher.get_stock_quote_yahoo('RELIANCE')
print(f"Live price: ₹{quote.get('price', 'N/A')}")
```

### Alpha Vantage (Free Tier Available)
```python
from nse_data_fetcher import NSEDataFetcher

# Get free API key from: https://www.alphavantage.co/
fetcher = NSEDataFetcher(alpha_vantage_key='YOUR_FREE_KEY')
quote = fetcher.get_stock_quote_alphavantage('RELIANCE')
```

## 📁 Generated Files

After running the demo, you'll have:
- `TCS_demo.xlsx` - Historical stock data with 30 days of OHLC
- `portfolio_demo.xlsx` - Portfolio tracking with current values
- `watchlist_demo.xlsx` - Stock watchlist template

Open these in Excel for further analysis, charting, or VBA automation!

## 🔧 Configuration (Optional)

For premium APIs (Dhan, Zerodha Kite, FMP):

1. Copy the environment template:
   ```bash
   cp .env.template .env
   ```

2. Edit `.env` and add your API keys:
   ```
   DHAN_CLIENT_ID=your_client_id
   KITE_API_KEY=your_api_key
   FMP_API_KEY=your_fmp_key
   ```

3. The configuration is automatically loaded when needed.

See [CONFIG.md](CONFIG.md) for detailed setup instructions.

## 📚 Next Steps

1. **Explore the code**: Look at `demo_app.py` to see how everything works
2. **Customize**: Modify the stock lists, time periods, or analysis methods
3. **Integrate**: Add your own analysis algorithms or trading strategies
4. **Automate**: Use Excel's VBA to automate report generation
5. **Scale**: Connect to premium APIs for real-time data

## 💡 Tips

- **No internet?** The mock data generator works completely offline
- **API limits?** Use mock data for development to save your API quota
- **Need help?** Check out the detailed documentation in CONFIG.md
- **Want more features?** See the example_usage.py for more code samples

## ❓ Common Questions

**Q: Do I need API keys to use this?**  
A: No! The application works perfectly with mock data for development and demonstration.

**Q: Is the mock data realistic?**  
A: Yes! It uses realistic base prices and volatility to simulate actual market behavior.

**Q: Can I use this for real trading?**  
A: This is for analysis and education. For trading, integrate with premium APIs and ensure proper risk management.

**Q: What if I want live data?**  
A: Yahoo Finance integration works without API keys. For other sources, see CONFIG.md.

## 🎉 You're Ready!

Run the demo and start exploring NSE stock market data:
```bash
python demo_app.py
```

The application is ready for peer review and further development!

---

**Developed by:** Mandar Bahadarpurkar  
**Repository:** https://github.com/mandarab76/ATS-NSE-Stock-Suite
