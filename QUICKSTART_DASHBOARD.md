# 🚀 Quick Start Guide - Dashboard

Get the ATS-NSE Stock Suite dashboard running in 5 minutes!

## Option 1: Run Locally (Fastest)

```bash
# Install dependencies
pip install -r requirements.txt

# Run dashboard
streamlit run dashboard.py
```

**Access**: Open browser to `http://localhost:8501`

**Mobile Access** (same network):
1. Find your IP: `ipconfig` (Windows) or `ifconfig` (Mac/Linux)
2. On mobile, go to: `http://YOUR_IP:8501`

## Option 2: Deploy to Cloud Run (Public Access)

### Prerequisites
- Google Cloud account ([Sign up free](https://cloud.google.com/free))
- GitHub account

### Steps

1. **Fork this repository** on GitHub

2. **Create Google Cloud Project**
   - Go to [console.cloud.google.com](https://console.cloud.google.com)
   - Create new project
   - Note the Project ID

3. **Enable APIs** (in Cloud Shell):
   ```bash
   gcloud services enable run.googleapis.com
   gcloud services enable cloudbuild.googleapis.com
   gcloud services enable artifactregistry.googleapis.com
   ```

4. **Create Artifact Registry**:
   ```bash
   gcloud artifacts repositories create ats-nse-stock-dashboard \
       --repository-format=docker \
       --location=us-central1
   ```

5. **Create Service Account**:
   ```bash
   # Create service account
   gcloud iam service-accounts create github-actions-deployer \
       --display-name="GitHub Actions Deployer"
   
   # Grant permissions (replace YOUR_PROJECT_ID)
   gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
       --member="serviceAccount:github-actions-deployer@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
       --role="roles/run.admin"
   
   gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
       --member="serviceAccount:github-actions-deployer@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
       --role="roles/storage.admin"
   
   gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
       --member="serviceAccount:github-actions-deployer@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
       --role="roles/artifactregistry.admin"
   
   gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
       --member="serviceAccount:github-actions-deployer@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
       --role="roles/iam.serviceAccountUser"
   
   # Create key
   gcloud iam service-accounts keys create key.json \
       --iam-account=github-actions-deployer@YOUR_PROJECT_ID.iam.gserviceaccount.com
   
   # Display key
   cat key.json
   ```

6. **Configure GitHub Secrets**:
   - Go to: Repository → Settings → Secrets and variables → Actions
   - Add secrets:
     - `GCP_PROJECT_ID`: Your Project ID
     - `GCP_SA_KEY`: Contents of key.json

7. **Deploy**:
   ```bash
   git push origin main
   ```

8. **Get URL**:
   - Go to Actions tab on GitHub
   - Click on the workflow run
   - Find the service URL in the summary

**Done!** 🎉 Your dashboard is live at: `https://ats-nse-stock-dashboard-xxxxx.run.app`

## Dashboard Features

### 📱 Mobile & Desktop
- Fully responsive design
- Works on any device with browser
- Touch-friendly interface

### 📊 Sections
1. **Market Overview** - Indices, top movers, 52-week highlights, news
2. **Stock Analysis** - Interactive charts, candlestick views
3. **Portfolio** - Track holdings, distribution chart
4. **Watchlist** - Monitor favorite stocks
5. **Settings** - Configure preferences
6. **Help** - Usage guide

### 💡 Features
- Real-time stock quotes
- Interactive Plotly charts
- Portfolio tracking
- Market news
- Global markets overview
- Mobile-optimized navigation

## Need Help?

- **Full Guide**: See [DEPLOYMENT.md](DEPLOYMENT.md)
- **Configuration**: See [CONFIG.md](CONFIG.md)
- **Issues**: [Create an issue](https://github.com/mandarab76/ATS-NSE-Stock-Suite/issues)

## Cost

Google Cloud Run free tier includes:
- 2 million requests/month FREE
- 360,000 GB-seconds FREE
- 180,000 vCPU-seconds FREE

**Most users stay within free tier!** 🎉

## Screenshots

The dashboard includes:
- 📈 Interactive candlestick charts
- 📊 Real-time market indices
- 🚀 Top gainers visualization
- 📉 Top losers tracking
- 💼 Portfolio pie charts
- 🌍 Global markets overview

---

**Ready to go? Run `streamlit run dashboard.py` now!** 🚀
