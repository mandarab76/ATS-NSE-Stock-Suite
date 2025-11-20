# ATS-NSE-Stock-Suite
NSE Stock Market Analysis Suite with Live Data Integration (Dhan API, Zerodha Kite, FMP) | VBA Automation | Excel Analytics | Developed by Mandar Bahadarpurkar

## Features
- **Live Data Integration**: Connect to multiple market data APIs (Dhan, Zerodha Kite, Financial Modeling Prep)
- **VBA Automation**: Excel-based automation for market analysis
- **Real-time Analytics**: Process and analyze NSE stock market data
- **Multiple API Support**: Flexible configuration for various data sources

## Quick Start

### 1. Configuration Setup

This project requires API credentials from various services. Follow these steps to configure:

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

### 2. Required API Keys

You'll need credentials from:
- **Dhan API**: Client ID and Access Token
- **Zerodha Kite**: API Key, Secret, and Access Token
- **Financial Modeling Prep (FMP)**: API Key
- **Hugging Face** (optional): Token and Space URL

See [CONFIG.md](CONFIG.md) for detailed instructions on obtaining these credentials.

### 3. Python Dependencies

Install required Python packages:
```bash
pip install python-dotenv
# Add other dependencies as needed
```

### 4. Using the Configuration

```python
from config_loader import config

# Access your credentials
dhan_client_id = config.DHAN_CLIENT_ID
kite_api_key = config.KITE_API_KEY
fmp_api_key = config.FMP_API_KEY

# Check configuration
if config.validate():
    print("Configuration is valid!")
```

## Project Structure

```
ATS-NSE-Stock-Suite/
├── .env.template       # Template for environment variables
├── .gitignore         # Git ignore rules (includes .env)
├── CONFIG.md          # Detailed configuration guide
├── SECRETS.md         # Document your tokens here (private repo)
├── config_loader.py   # Python configuration loader
└── README.md          # This file
```

## Documentation

- **[CONFIG.md](CONFIG.md)**: Complete guide for setting up API credentials
- **[SECRETS.md](SECRETS.md)**: Template for documenting your tokens (private repo only)

## Security Notes

- The `.env` file is excluded from git (via `.gitignore`)
- Never commit API keys to version control
- Rotate your API keys regularly
- Monitor API usage for unusual activity

## Support

For issues related to:
- **API credentials**: Contact the respective API provider
- **Configuration**: See [CONFIG.md](CONFIG.md)
- **Project setup**: Open an issue in this repository

## About

Developed by Mandar Bahadarpurkar for NSE stock market analysis and automation.
