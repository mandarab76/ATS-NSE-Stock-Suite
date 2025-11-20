# Hugging Face Integration Guide

## About Connecting to Hugging Face Spaces

You mentioned wanting to pull secret tokens from your Hugging Face Space. Unfortunately, I cannot directly connect to your Hugging Face Space to retrieve secrets. However, I can help you set up the integration manually.

## How to Get Your Hugging Face Tokens

### Method 1: From Hugging Face Settings (Recommended)

1. **Go to your Hugging Face Settings**:
   - Visit https://huggingface.co/settings/tokens
   - Log in if needed

2. **Create or Copy an Access Token**:
   - Click "New token" if you need a new one
   - Or copy an existing token
   - Choose appropriate permissions (read/write)

3. **Add to your .env file**:
   ```env
   HUGGINGFACE_TOKEN=hf_your_token_here
   ```

### Method 2: From Your Hugging Face Space

If you have secrets stored in a Hugging Face Space:

1. **Access your Space**:
   - Go to https://huggingface.co/spaces/[your-username]/[your-space]
   - Click on "Settings" tab

2. **View Repository Secrets**:
   - Scroll to "Repository secrets" section
   - Copy the secret values you need

3. **Document them here** (since this is a private repo):
   - Paste them in `SECRETS.md`
   - Or directly in your `.env` file

## What You Need to Share

Since this is a private repository and you mentioned you don't mind sharing tokens, please provide:

### 1. Hugging Face Token
- **Location**: https://huggingface.co/settings/tokens
- **What to share**: The token string starting with `hf_`
- **Paste here**: [Your token]

### 2. Hugging Face Space URL (if applicable)
- **Format**: `https://huggingface.co/spaces/username/spacename`
- **Paste here**: [Your space URL]

### 3. Any Space Secrets
If your Space has specific secrets you want to use in this project:
- **Secret Name**: [Name]
- **Secret Value**: [Value]

## Using Hugging Face API in Your Code

Once configured, you can use the Hugging Face Hub API:

```python
from config_loader import config
from huggingface_hub import HfApi

# Initialize the API
api = HfApi(token=config.HUGGINGFACE_TOKEN)

# Access your space or models
# Example: Download a model
api.snapshot_download(repo_id="your-repo-id")

# Example: Upload to a space
api.upload_file(
    path_or_fileobj="local_file.txt",
    path_in_repo="remote_file.txt",
    repo_id="username/spacename",
    repo_type="space"
)
```

## For Private Repository Sharing

Since you mentioned this is a private repo and you're comfortable sharing tokens:

### Option A: Paste Directly in SECRETS.md

Edit `SECRETS.md` and add your tokens there. Example:

```markdown
### Hugging Face
- **Token**: hf_xxxxxxxxxxxxxxxxxxxxxxxxxxx
- **Space URL**: https://huggingface.co/spaces/mandarab76/your-space-name
```

### Option B: Create .env File Now

```bash
# Copy template
cp .env.template .env

# Add your tokens
echo "HUGGINGFACE_TOKEN=hf_your_actual_token_here" >> .env
echo "HUGGINGFACE_SPACE_URL=https://huggingface.co/spaces/your-space" >> .env
```

## Security Considerations

Even in a private repo:

1. **Repository Access**: Only share access with trusted collaborators
2. **Token Scope**: Use tokens with minimal required permissions
3. **Token Rotation**: Rotate tokens periodically
4. **Monitor Usage**: Check Hugging Face dashboard for unusual activity
5. **Backup**: Keep a secure backup of important tokens

## Next Steps

1. **Get your tokens** from Hugging Face (methods above)
2. **Choose where to store them**:
   - In `.env` file (not committed to git)
   - In `SECRETS.md` (committed, but private repo)
   - Or tell me directly here in this conversation
3. **Configure your project** using the tokens
4. **Test the integration** with the example code above

## Need Help?

If you'd like to share your tokens directly:
- You can paste them in a comment or message
- Or add them to `SECRETS.md`
- Or create the `.env` file with the tokens

Since this is a private repository, any of these methods are secure as long as the repository remains private.

## Why I Can't Connect Directly

As an AI assistant, I don't have the capability to:
- Log into your Hugging Face account
- Access your Hugging Face Spaces directly
- Read secrets from your Spaces programmatically

I can only work with information you provide directly in this repository or conversation.

## Alternative: Share Here

If you want to share your tokens, you can paste them here and I'll help you:
1. Add them to the appropriate configuration files
2. Set up the integration properly
3. Create example code to use them

Just provide:
- Hugging Face Token: `hf_...`
- Space URL (if needed): `https://...`
- Any other API tokens you mentioned (Dhan, Kite, FMP)
