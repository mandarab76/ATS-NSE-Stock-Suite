# 🚀 Deployment Guide for ATS-NSE Stock Suite Dashboard

This guide provides step-by-step instructions for deploying the ATS-NSE Stock Suite dashboard to Google Cloud Run.

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Local Testing](#local-testing)
- [Google Cloud Setup](#google-cloud-setup)
- [GitHub Secrets Configuration](#github-secrets-configuration)
- [Deployment Methods](#deployment-methods)
- [Accessing Your Dashboard](#accessing-your-dashboard)
- [Troubleshooting](#troubleshooting)
- [Cost Information](#cost-information)

## Prerequisites

### Required Accounts
- **Google Cloud Account**: [Sign up here](https://cloud.google.com/free)
- **GitHub Account**: For automated deployments
- **Credit Card**: Required for GCP (free tier available)

### Required Tools (for manual deployment)
- **gcloud CLI**: [Installation guide](https://cloud.google.com/sdk/docs/install)
- **Docker**: [Installation guide](https://docs.docker.com/get-docker/)
- **Git**: [Installation guide](https://git-scm.com/downloads)

## 🧪 Local Testing

Before deploying to Cloud Run, test the dashboard locally:

### Option 1: Run with Python

```bash
# Install dependencies
pip install -r requirements.txt

# Run dashboard
streamlit run dashboard.py
```

Access at: `http://localhost:8501`

### Option 2: Run with Docker

```bash
# Build Docker image
docker build -t ats-nse-dashboard .

# Run container
docker run -p 8080:8080 ats-nse-dashboard
```

Access at: `http://localhost:8080`

### Test on Mobile (Local Network)

1. Find your computer's IP address:
   - **Windows**: `ipconfig` → Look for IPv4 Address
   - **Mac/Linux**: `ifconfig` → Look for inet address

2. Access from mobile device on same network:
   - Go to: `http://YOUR_IP_ADDRESS:8501`

## ☁️ Google Cloud Setup

### Step 1: Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click on project dropdown → "New Project"
3. Enter project name (e.g., "ats-nse-stock-suite")
4. Note your **Project ID** (you'll need this later)

### Step 2: Enable Required APIs

Run these commands in [Cloud Shell](https://console.cloud.google.com/cloudshell) or local terminal:

```bash
# Set your project ID
export PROJECT_ID="your-project-id-here"
gcloud config set project $PROJECT_ID

# Enable required APIs
gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com
gcloud services enable artifactregistry.googleapis.com
```

### Step 3: Create Artifact Registry Repository

```bash
# Create Docker repository
gcloud artifacts repositories create ats-nse-stock-dashboard \
    --repository-format=docker \
    --location=us-central1 \
    --description="ATS NSE Stock Dashboard container images"
```

### Step 4: Create Service Account for GitHub Actions

```bash
# Create service account
gcloud iam service-accounts create github-actions-deployer \
    --display-name="GitHub Actions Deployer" \
    --description="Service account for GitHub Actions to deploy to Cloud Run"

# Grant permissions
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:github-actions-deployer@${PROJECT_ID}.iam.gserviceaccount.com" \
    --role="roles/run.admin"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:github-actions-deployer@${PROJECT_ID}.iam.gserviceaccount.com" \
    --role="roles/storage.admin"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:github-actions-deployer@${PROJECT_ID}.iam.gserviceaccount.com" \
    --role="roles/artifactregistry.admin"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:github-actions-deployer@${PROJECT_ID}.iam.gserviceaccount.com" \
    --role="roles/iam.serviceAccountUser"

# Create and download key
gcloud iam service-accounts keys create ~/github-actions-key.json \
    --iam-account=github-actions-deployer@${PROJECT_ID}.iam.gserviceaccount.com

# Display the key (copy this for GitHub secrets)
cat ~/github-actions-key.json
```

⚠️ **Important**: Keep this JSON key secure! You'll add it to GitHub secrets.

## 🔐 GitHub Secrets Configuration

### Step 1: Add Required Secrets

1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add the following secrets:

#### Required Secrets:

| Secret Name | Value | Description |
|------------|-------|-------------|
| `GCP_PROJECT_ID` | your-project-id | Your Google Cloud Project ID |
| `GCP_SA_KEY` | {JSON key content} | Service account key JSON (entire content) |

#### Optional API Secrets (for live data):

| Secret Name | Description |
|------------|-------------|
| `ALPHA_VANTAGE_API_KEY` | Alpha Vantage API key |
| `FMP_API_KEY` | Financial Modeling Prep API key |
| `DHAN_CLIENT_ID` | Dhan API client ID |
| `DHAN_ACCESS_TOKEN` | Dhan API access token |
| `KITE_API_KEY` | Zerodha Kite API key |
| `KITE_API_SECRET` | Zerodha Kite API secret |
| `KITE_ACCESS_TOKEN` | Zerodha Kite access token |

### Step 2: Verify Secrets

After adding secrets, verify they're configured:
- Go to **Settings** → **Secrets and variables** → **Actions**
- You should see all your secrets listed (values are hidden)

## 🚀 Deployment Methods

### Method 1: Automatic Deployment (Recommended)

The easiest way to deploy is using GitHub Actions:

1. **Make any change and push to main branch**:
   ```bash
   git add .
   git commit -m "Deploy to Cloud Run"
   git push origin main
   ```

2. **Monitor deployment**:
   - Go to your GitHub repository
   - Click **Actions** tab
   - Watch the "Deploy to Google Cloud Run" workflow

3. **Get your URL**:
   - Once complete, check the workflow summary for your service URL
   - Format: `https://ats-nse-stock-dashboard-XXXXX.run.app`

### Method 2: Manual Deployment

#### Via gcloud CLI:

```bash
# Authenticate
gcloud auth login
gcloud config set project YOUR_PROJECT_ID

# Deploy directly from source
gcloud run deploy ats-nse-stock-dashboard \
    --source . \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --memory 1Gi \
    --cpu 1 \
    --port 8080 \
    --set-env-vars "ALPHA_VANTAGE_API_KEY=your_key,FMP_API_KEY=your_key"
```

#### Via Docker:

```bash
# Build image
docker build -t gcr.io/YOUR_PROJECT_ID/ats-nse-dashboard .

# Push to Google Container Registry
docker push gcr.io/YOUR_PROJECT_ID/ats-nse-dashboard

# Deploy to Cloud Run
gcloud run deploy ats-nse-stock-dashboard \
    --image gcr.io/YOUR_PROJECT_ID/ats-nse-dashboard \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated
```

### Method 3: Google Cloud Console

1. Go to [Cloud Run Console](https://console.cloud.google.com/run)
2. Click **Create Service**
3. Select **Deploy one revision from an existing container image**
4. Choose your container image or use "Continuously deploy new revisions from a source repository"
5. Configure:
   - Service name: `ats-nse-stock-dashboard`
   - Region: `us-central1`
   - Authentication: Allow unauthenticated invocations
   - Container port: `8080`
   - Memory: `1 GiB`
   - CPU: `1`
6. Click **Create**

## 📱 Accessing Your Dashboard

Once deployed, you'll receive a URL like:
```
https://ats-nse-stock-dashboard-xxxxx-uc.a.run.app
```

### Access From:
- ✅ **Desktop Browser**: Full interactive experience
- ✅ **Mobile Browser**: Responsive mobile layout
- ✅ **Tablet**: Optimized for medium screens
- ✅ **Any Device**: With internet access

### Features Available:
1. **Market Overview** - Real-time indices and top movers
2. **Stock Analysis** - Interactive charts and analysis
3. **Portfolio Tracking** - Monitor your investments
4. **Watchlist** - Track favorite stocks
5. **Settings** - Configure preferences
6. **Help** - Usage documentation

## 🔧 Troubleshooting

### Issue: Service not accessible

**Solution 1**: Check if service allows unauthenticated access
```bash
gcloud run services add-iam-policy-binding ats-nse-stock-dashboard \
    --region=us-central1 \
    --member="allUsers" \
    --role="roles/run.invoker"
```

### Issue: Build fails in GitHub Actions

**Check**:
1. Verify `GCP_PROJECT_ID` secret is correct
2. Ensure `GCP_SA_KEY` contains valid JSON
3. Check that Artifact Registry repository exists
4. Review workflow logs for specific errors

### Issue: Container fails to start

**Check logs**:
```bash
gcloud run services logs read ats-nse-stock-dashboard \
    --region=us-central1 \
    --limit=50
```

### Issue: "Permission Denied" errors

**Solution**: Grant additional permissions to service account
```bash
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
    --member="serviceAccount:github-actions-deployer@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/cloudbuild.builds.builder"
```

### Issue: Slow loading on mobile

**Solutions**:
1. Check network connection
2. Service may be cold-starting (first request takes longer)
3. Consider increasing min instances:
   ```bash
   gcloud run services update ats-nse-stock-dashboard \
       --region=us-central1 \
       --min-instances=1
   ```

## 💰 Cost Information

### Google Cloud Run Pricing (as of 2024)

**Free Tier (Monthly)**:
- 2 million requests
- 360,000 GB-seconds
- 180,000 vCPU-seconds
- 1 GB network egress

**Estimated Costs** (for this dashboard):
- **Light usage** (< 10,000 requests/month): **FREE**
- **Medium usage** (100,000 requests/month): **~$5-10/month**
- **Heavy usage** (1,000,000 requests/month): **~$30-50/month**

### Cost Optimization Tips:

1. **Set minimum instances to 0** (default):
   - Service scales to zero when not in use
   - No charges when idle

2. **Use mock data** for demos:
   - Reduces external API costs
   - Faster response times

3. **Enable request throttling**:
   - Prevents abuse and unexpected charges

4. **Monitor usage**:
   ```bash
   gcloud run services describe ats-nse-stock-dashboard \
       --region=us-central1 \
       --format="value(status.url)"
   ```

5. **Set budget alerts** in Google Cloud Console

## 📊 Monitoring and Maintenance

### View Service Details:
```bash
gcloud run services describe ats-nse-stock-dashboard \
    --region=us-central1
```

### View Logs:
```bash
gcloud run services logs tail ats-nse-stock-dashboard \
    --region=us-central1
```

### Update Service:
```bash
# Update environment variables
gcloud run services update ats-nse-stock-dashboard \
    --region=us-central1 \
    --set-env-vars "NEW_VAR=value"

# Update resources
gcloud run services update ats-nse-stock-dashboard \
    --region=us-central1 \
    --memory=2Gi \
    --cpu=2
```

### Delete Service:
```bash
gcloud run services delete ats-nse-stock-dashboard \
    --region=us-central1
```

## 🎉 Success Checklist

- [ ] Dashboard runs locally without errors
- [ ] Google Cloud project created and APIs enabled
- [ ] Service account created with proper permissions
- [ ] GitHub secrets configured
- [ ] First deployment successful
- [ ] Dashboard accessible from mobile and desktop
- [ ] API keys configured (if using live data)
- [ ] Budget alerts set up
- [ ] Monitoring configured

## 📞 Support

For issues or questions:
- **GitHub Issues**: [Create an issue](https://github.com/mandarab76/ATS-NSE-Stock-Suite/issues)
- **Documentation**: Check README.md and CONFIG.md
- **Google Cloud Support**: [GCP Support](https://cloud.google.com/support)

## 🔗 Useful Links

- [Google Cloud Run Documentation](https://cloud.google.com/run/docs)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly Documentation](https://plotly.com/python/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

---

**Happy Deploying! 🚀**
