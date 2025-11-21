# Installation & Deployment Guide
# ATS-NSE-Stock-Suite v1.0.0 - Production Release

## 📦 Package Information

**Package Name**: ATS-NSE-Stock-Suite-v1.0.0-production.zip  
**Size**: ~39 KB  
**Version**: 1.0.0  
**Release Date**: November 2025  
**Status**: ✅ Production Ready

## 🚀 Quick Installation

### For End Users (Simple Installation)

1. **Download & Extract**
   ```bash
   # Extract the zip file
   unzip ATS-NSE-Stock-Suite-v1.0.0-production.zip
   cd ATS-NSE-Stock-Suite
   ```

2. **Run Auto Setup**
   ```bash
   # Run the production setup script
   python3 setup_production.py
   ```
   
   This script will:
   - Check Python version (requires 3.8+)
   - Install all dependencies automatically
   - Create configuration files
   - Run tests to verify installation
   - Provide next steps

3. **Start Using**
   ```bash
   # Run the demo to see it in action
   python demo_app.py
   ```

### For Developers (Manual Installation)

1. **Extract Package**
   ```bash
   unzip ATS-NSE-Stock-Suite-v1.0.0-production.zip
   cd ATS-NSE-Stock-Suite
   ```

2. **Create Virtual Environment (Recommended)**
   ```bash
   # Create virtual environment
   python3 -m venv venv
   
   # Activate it
   source venv/bin/activate  # On Linux/Mac
   # OR
   venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify Installation**
   ```bash
   # Run integration tests
   python test_integration.py
   
   # Should output: "Tests passed: 6/6"
   ```

## 📋 System Requirements

### Minimum Requirements
- **Python**: 3.8 or higher
- **pip**: Latest version
- **Disk Space**: 50 MB
- **RAM**: 512 MB
- **OS**: Windows, Linux, macOS

### Recommended
- **Python**: 3.10+
- **RAM**: 2 GB
- **Internet**: For live API access (optional)

## 📚 What's Included

### Core Modules (7 Python files)
- `nse_data_fetcher.py` - Live API integration
- `mock_nse_data.py` - Mock data generator
- `excel_integration.py` - Excel exports
- `demo_app.py` - Complete demo
- `config_loader.py` - Configuration
- `example_usage.py` - Examples
- `test_integration.py` - Tests

### Configuration
- `.env.template` - Configuration template
- `requirements.txt` - Dependencies
- `setup_production.py` - Auto setup script

### Documentation (7 files)
- `README.md` - Main documentation
- `QUICKSTART.md` - Quick start guide
- `RELEASE_NOTES.md` - Release information
- `PROJECT_SUMMARY.md` - Project overview
- `CONFIG.md` - API configuration
- `HUGGINGFACE_GUIDE.md` - HF integration
- `SECRETS.md` - Secrets template

## ⚙️ Configuration (Optional)

The application works out-of-the-box with mock data. To enable live APIs:

1. **Copy the template**
   ```bash
   cp .env.template .env
   ```

2. **Edit .env and add your API keys**
   ```
   # For Yahoo Finance - No key needed (free)
   # For Alpha Vantage - Get free key at: https://www.alphavantage.co/
   
   # Optional premium APIs
   DHAN_CLIENT_ID=your_dhan_client_id
   DHAN_ACCESS_TOKEN=your_dhan_token
   KITE_API_KEY=your_kite_key
   FMP_API_KEY=your_fmp_key
   ```

3. **See CONFIG.md for detailed setup instructions**

## 🧪 Testing & Verification

### Quick Test
```bash
python demo_app.py
```

Expected output:
- Stock quotes for 5 NSE stocks
- Historical data (30 days)
- Portfolio tracking
- Market analysis
- Excel file generation

### Full Test Suite
```bash
python test_integration.py
```

Expected output:
```
Tests passed: 6/6
🎉 All tests passed! Application is ready for peer review.
```

### Manual Testing
```python
# Test mock data
from mock_nse_data import MockNSEData
mock = MockNSEData()
quote = mock.get_stock_quote('RELIANCE')
print(f"Price: ₹{quote['price']:.2f}")

# Test Excel export
from excel_integration import ExcelExporter
exporter = ExcelExporter()
exporter.export_stock_quote(quote, filename="test.xlsx")
```

## 🌐 Deployment Options

### Option 1: Local Development
- Extract and run on local machine
- Use mock data for development
- No internet required

### Option 2: Server Deployment
```bash
# On server
cd /opt/
unzip ATS-NSE-Stock-Suite-v1.0.0-production.zip
cd ATS-NSE-Stock-Suite
python3 setup_production.py

# Add to cron for scheduled runs
crontab -e
# Add: 0 9 * * 1-5 /usr/bin/python3 /opt/ATS-NSE-Stock-Suite/demo_app.py
```

### Option 3: Docker Deployment
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY ATS-NSE-Stock-Suite/ /app/
RUN pip install -r requirements.txt
CMD ["python", "demo_app.py"]
```

### Option 4: Cloud Deployment
- **AWS**: Use EC2 or Lambda
- **Azure**: Use App Service
- **Google Cloud**: Use Cloud Functions
- **Heroku**: Use Heroku Dynos

## 🔒 Security Notes

1. **Never commit .env file**
   - Already in .gitignore
   - Contains sensitive API keys

2. **Rotate API keys regularly**
   - Change keys every 90 days
   - Monitor API usage

3. **Use read-only keys when possible**
   - Limit permissions
   - Reduce risk

4. **Monitor logs**
   - Check for unusual activity
   - Set up alerts

## 🆘 Troubleshooting

### "No module named 'pandas'"
```bash
pip install pandas openpyxl
```

### "Python version incompatible"
```bash
# Install Python 3.8 or higher
python3 --version  # Check current version
```

### "Tests failing"
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### "API errors"
- Mock data works without APIs
- Check internet connection for live APIs
- Verify API keys in .env file

### "Excel files not generating"
```bash
# Install openpyxl
pip install openpyxl
```

## 📞 Support

### Documentation
- README.md - Overview
- QUICKSTART.md - Quick start
- CONFIG.md - API setup
- PROJECT_SUMMARY.md - Architecture

### Issues
Open an issue on GitHub with:
- Python version
- OS version
- Error message
- Steps to reproduce

## ✅ Production Checklist

Before deploying to production:

- [ ] Python 3.8+ installed
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Tests passing (`python test_integration.py`)
- [ ] Configuration reviewed (`.env` file)
- [ ] API keys secured (if using live APIs)
- [ ] Documentation reviewed
- [ ] Demo runs successfully (`python demo_app.py`)
- [ ] Backup strategy in place
- [ ] Monitoring set up (optional)
- [ ] Error handling tested
- [ ] Performance acceptable

## 🎉 Success!

If all tests pass and demo runs successfully, your installation is complete!

### Next Steps
1. Read QUICKSTART.md for usage examples
2. Run demo_app.py to see features
3. Configure API keys (optional)
4. Start building your analysis tools
5. Integrate with Excel/VBA

---

**Package**: ATS-NSE-Stock-Suite v1.0.0  
**Status**: ✅ Production Ready  
**Developer**: Mandar Bahadarpurkar  
**Release**: November 2025
