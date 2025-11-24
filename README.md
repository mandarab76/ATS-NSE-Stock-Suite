# ATS-NSE-Stock-Suite

[![Deploy to Cloud Run](https://github.com/mandarab76/ATS-NSE-Stock-Suite/actions/workflows/deploy-cloudrun.yml/badge.svg)](https://github.com/mandarab76/ATS-NSE-Stock-Suite/actions/workflows/deploy-cloudrun.yml)

NSE Stock Market Analysis Suite with Live Data Integration (Dhan API, Zerodha Kite, FMP) | VBA Automation | Excel Analytics | Developed by Mandar Bahadarpurkar

## ✨ Features
- **📱 Mobile-Friendly Dashboard**: Responsive Streamlit web dashboard optimized for mobile and desktop
- **📊 Interactive Charts**: Advanced Plotly visualizations with candlestick, line, and bar charts
- **🏠 Market Overview**: Real-time indices, top gainers/losers, 52-week highlights, and global markets
- **💼 Portfolio Management**: Track holdings, performance, and analyze portfolio distribution
- **👁️ Watchlist**: Monitor your favorite stocks in real-time
- **☁️ Cloud Deployment**: Ready to deploy on Google Cloud Run with automated CI/CD
- **Live Data Integration**: Connect to multiple market data APIs (Dhan, Zerodha Kite, Financial Modeling Prep, Yahoo Finance, Alpha Vantage)
- **Mock Data Support**: Built-in mock data generator for development and demonstration without API keys
- **Excel Integration**: Export stock data, historical analysis, and portfolio tracking to Excel
- **Multiple API Support**: Flexible configuration for various data sources

## 🌐 Live Dashboard

### ⚡ Quick Start

**New to the dashboard?** See [QUICKSTART_DASHBOARD.md](QUICKSTART_DASHBOARD.md) for a 5-minute setup guide!

### Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run dashboard.py
```

The dashboard will open in your browser at `http://localhost:8501`. It's fully responsive and works on mobile devices!

### Access on Mobile/Browser

1. **Local Network**: Access from any device on your network using your computer's IP address:
   - Find your IP: `ipconfig` (Windows) or `ifconfig` (Mac/Linux)
   - Access from mobile: `http://YOUR_IP:8501`

2. **Cloud Deployment**: Deploy to Google Cloud Run for public access (see deployment section below)

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
├── .github/
│   └── workflows/
│       └── deploy-cloudrun.yml  # GitHub Actions workflow for Cloud Run deployment
├── .env.template                 # Template for environment variables
├── .gitignore                    # Git ignore rules (includes .env)
├── .dockerignore                 # Docker build exclusions
├── Dockerfile                    # Docker container configuration for Cloud Run
├── dashboard.py                  # 📱 Mobile-friendly Streamlit dashboard (NEW!)
├── config_loader.py              # Python configuration loader
├── nse_data_fetcher.py          # Live API data fetcher (Yahoo Finance, Alpha Vantage)
├── mock_nse_data.py             # Mock data generator for development/demo
├── excel_integration.py         # Excel export and reporting functionality
├── demo_app.py                  # Complete demonstration application
├── example_usage.py             # Usage examples for configuration
├── requirements.txt             # Python dependencies (includes Streamlit & Plotly)
├── CONFIG.md                    # Detailed configuration guide
├── SECRETS.md                   # Document your tokens here (private repo)
├── HUGGINGFACE_GUIDE.md        # Hugging Face integration guide
└── README.md                   # This file
```


## 🎯 Main Scripts

- **dashboard.py**: 📱 **Mobile-friendly web dashboard** - Main application with responsive UI
- **demo_app.py**: Complete demonstration of all features - Command-line demo
- **mock_nse_data.py**: Generate realistic stock data without API keys
- **nse_data_fetcher.py**: Fetch live data from Yahoo Finance and other APIs
- **excel_integration.py**: Export data to Excel for analysis
- **config_loader.py**: Manage API credentials and configuration

## 📊 Dashboard Output

The web dashboard provides:
- **📱 Mobile-responsive interface** accessible from any device
- **📊 Interactive Plotly charts** with zoom, pan, and hover features
- **🏠 Market overview** with real-time indices, top movers, and global markets
- **💼 Portfolio tracking** with distribution charts and performance metrics
- **👁️ Watchlist** for monitoring favorite stocks
- **📈 Advanced charting** including candlestick, line, and bar charts

The command-line demo application generates:
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

```

## ☁️ Deploy to Google Cloud Run

### Prerequisites

1. **Google Cloud Account**: Sign up at [cloud.google.com](https://cloud.google.com)
2. **GCP Project**: Create a new project or use an existing one
3. **Enable APIs**:
   - Cloud Run API
   - Cloud Build API
   - Artifact Registry API

### Setup Instructions

#### 1. Create Google Cloud Project

```bash
# Install gcloud CLI (if not already installed)
# Visit: https://cloud.google.com/sdk/docs/install

# Login to Google Cloud
gcloud auth login

# Create a new project
gcloud projects create YOUR_PROJECT_ID --name="ATS NSE Stock Suite"

# Set the project
gcloud config set project YOUR_PROJECT_ID

# Enable required APIs
gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com
gcloud services enable artifactregistry.googleapis.com
```

#### 2. Create Artifact Registry Repository

```bash
# Create repository for Docker images
gcloud artifacts repositories create ats-nse-stock-dashboard \
    --repository-format=docker \
    --location=us-central1 \
    --description="ATS NSE Stock Dashboard container images"
```

#### 3. Configure GitHub Secrets

Go to your GitHub repository Settings → Secrets and Variables → Actions, and add:

- `GCP_PROJECT_ID`: Your Google Cloud Project ID
- `GCP_SA_KEY`: Service account JSON key (see below)
- `ALPHA_VANTAGE_API_KEY`: (Optional) Your Alpha Vantage API key
- `FMP_API_KEY`: (Optional) Your FMP API key
- `DHAN_CLIENT_ID`: (Optional) Your Dhan client ID
- `DHAN_ACCESS_TOKEN`: (Optional) Your Dhan access token
- `KITE_API_KEY`: (Optional) Your Kite API key
- `KITE_API_SECRET`: (Optional) Your Kite API secret
- `KITE_ACCESS_TOKEN`: (Optional) Your Kite access token

#### 4. Create Service Account

```bash
# Create service account
gcloud iam service-accounts create github-actions-deployer \
    --display-name="GitHub Actions Deployer"

# Grant necessary permissions
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
    --member="serviceAccount:github-actions-deployer@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/run.admin"

gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
    --member="serviceAccount:github-actions-deployer@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/storage.admin"

gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
    --member="serviceAccount:github-actions-deployer@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/artifactregistry.admin"

# Create and download service account key
gcloud iam service-accounts keys create key.json \
    --iam-account=github-actions-deployer@YOUR_PROJECT_ID.iam.gserviceaccount.com

# Copy the contents of key.json to GitHub secret GCP_SA_KEY
cat key.json
```

#### 5. Deploy

##### Option A: Automatic Deployment via GitHub Actions

Push to `main` or `master` branch, and the workflow will automatically:
1. Build the Docker image
2. Push to Google Artifact Registry
3. Deploy to Cloud Run
4. Output the service URL

```bash
git add .
git commit -m "Deploy dashboard to Cloud Run"
git push origin main
```

##### Option B: Manual Deployment

```bash
# Build and deploy manually
gcloud run deploy ats-nse-stock-dashboard \
    --source . \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --memory 1Gi \
    --cpu 1 \
    --port 8080
```

#### 6. Access Your Dashboard

After deployment, you'll get a URL like:
```
https://ats-nse-stock-dashboard-XXXXX.run.app
```

This URL is accessible from:
- ✅ Any web browser (desktop/laptop)
- ✅ Mobile devices (iOS/Android)
- ✅ Tablets
- ✅ Any device with internet access

### Dashboard Features

#### 📱 Mobile-Optimized Interface

- **Responsive Design**: Automatically adapts to screen size
- **Touch-Friendly**: Optimized for touch interactions
- **Horizontal Tabs**: Easy navigation on mobile devices
- **Hamburger Menu**: Access all features from sidebar

#### 📊 Dashboard Sections

1. **Market Overview** 🏠
   - Major indices (NIFTY 50, BANK NIFTY)
   - Top gainers and losers
   - 52-week high/low highlights
   - Surprise stocks of the day
   - Market news
   - Global markets (S&P 500, NASDAQ, FTSE, Nikkei, Hang Seng)

2. **Stock Analysis** 📊
   - Individual stock analysis
   - Interactive candlestick charts
   - Volume analysis
   - Price trend visualization
   - Real-time quotes

3. **Portfolio** 💼
   - Track your holdings
   - Portfolio value calculation
   - Distribution pie chart
   - Performance metrics

4. **Watchlist** 👁️
   - Monitor favorite stocks
   - Real-time price updates
   - Quick access to key metrics

5. **Settings** ⚙️
   - Data source selection
   - Display preferences
   - API configuration

6. **Help** ❓
   - Getting started guide
   - Navigation instructions
   - Support information

### Cost Optimization

Google Cloud Run offers generous free tier:
- **2 million requests/month** free
- **360,000 GB-seconds** free
- **180,000 vCPU-seconds** free

For this dashboard with moderate usage, you'll likely stay within the free tier!

### Monitoring and Logs

View logs and monitor your deployment:

```bash
# View logs
gcloud run services logs tail ats-nse-stock-dashboard --region=us-central1

# Check service status
gcloud run services describe ats-nse-stock-dashboard --region=us-central1
```

## 📚 Documentation

- **[QUICKSTART_DASHBOARD.md](QUICKSTART_DASHBOARD.md)**: ⚡ **5-minute dashboard setup** (START HERE!)
- **[DEPLOYMENT.md](DEPLOYMENT.md)**: 🚀 **Complete Cloud Run deployment guide**
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
