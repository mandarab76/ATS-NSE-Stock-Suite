# Configuration Guide

This document explains how to configure the API keys and tokens required for the ATS-NSE-Stock-Suite.

## Setting Up Your Configuration

### Step 1: Create Your .env File

1. Copy the `.env.template` file to create a new `.env` file:
   ```bash
   cp .env.template .env
   ```

2. Open the `.env` file and fill in your actual API keys and tokens.

### Step 2: Obtain API Keys

#### Dhan API
- **Website**: https://dhan.co/
- **Documentation**: https://api.dhan.co/
- Required credentials:
  - `DHAN_CLIENT_ID`: Your Dhan client ID
  - `DHAN_ACCESS_TOKEN`: Your Dhan access token

#### Zerodha Kite API
- **Website**: https://kite.trade/
- **Documentation**: https://kite.trade/docs/connect/v3/
- Required credentials:
  - `KITE_API_KEY`: Your Kite API key
  - `KITE_API_SECRET`: Your Kite API secret
  - `KITE_ACCESS_TOKEN`: Your Kite access token (generated after login flow)

#### Financial Modeling Prep (FMP)
- **Website**: https://financialmodelingprep.com/
- **Documentation**: https://site.financialmodelingprep.com/developer/docs
- Required credentials:
  - `FMP_API_KEY`: Your FMP API key

#### Hugging Face (Optional)
- **Website**: https://huggingface.co/
- **Documentation**: https://huggingface.co/docs
- Required credentials:
  - `HUGGINGFACE_TOKEN`: Your Hugging Face access token
  - `HUGGINGFACE_SPACE_URL`: URL to your Hugging Face space

### Step 3: Verify Configuration

After setting up your `.env` file, ensure:
1. The file is not tracked by git (it's in `.gitignore`)
2. All required tokens are filled in
3. No spaces around the `=` sign in the `.env` file
4. Tokens are kept secure and not shared publicly

## Security Best Practices

Even though this is a private repository, follow these security practices:

1. **Never commit the .env file**: The `.gitignore` file is configured to exclude it
2. **Use environment-specific files**: Create `.env.development`, `.env.production` etc. as needed
3. **Rotate keys regularly**: Update your API keys periodically
4. **Limit key permissions**: Use read-only keys where possible
5. **Monitor API usage**: Check your API dashboards for unusual activity

## Sharing Tokens in a Private Repository

Since this is a private repository and you need to share tokens with the development environment:

### Option 1: Direct .env File (Recommended for Private Repos)
Create the `.env` file directly with your tokens. It will be ignored by git but available locally.

### Option 2: Documentation
Document your tokens in this file or in a separate secure note, then manually create the `.env` file.

### Option 3: GitHub Secrets (For CI/CD)
If you're using GitHub Actions or similar, add your tokens as repository secrets:
1. Go to Settings → Secrets and variables → Actions
2. Add each token as a secret
3. Reference them in your workflows

## Example .env File

```env
# Dhan API
DHAN_CLIENT_ID=1234567890
DHAN_ACCESS_TOKEN=abcdef1234567890

# Zerodha Kite API
KITE_API_KEY=your_api_key
KITE_API_SECRET=your_api_secret
KITE_ACCESS_TOKEN=your_access_token

# FMP API
FMP_API_KEY=your_fmp_key

# Hugging Face
HUGGINGFACE_TOKEN=hf_your_token_here
HUGGINGFACE_SPACE_URL=https://huggingface.co/spaces/your-space

# Configuration
DEBUG_MODE=True
LOG_LEVEL=DEBUG
```

## Troubleshooting

### Token Not Found Errors
- Verify the `.env` file is in the project root directory
- Check that environment variable names match exactly
- Ensure there are no quotes around values unless required

### API Authentication Errors
- Verify tokens are current and not expired
- Check API key permissions on the provider's dashboard
- Ensure your IP is not blocked by the API provider

### Loading .env Files in Python
Use the `python-dotenv` library:

```python
from dotenv import load_dotenv
import os

load_dotenv()

dhan_client_id = os.getenv('DHAN_CLIENT_ID')
kite_api_key = os.getenv('KITE_API_KEY')
```

## Support

For issues with:
- **API keys**: Contact the respective API provider
- **Configuration setup**: Refer to this guide or raise an issue in the repository
