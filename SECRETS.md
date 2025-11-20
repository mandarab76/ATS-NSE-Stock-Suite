# API Secrets and Tokens

**Note**: This file is for documenting your actual API tokens since this is a private repository. 
You can paste your tokens here for reference, but it's recommended to use the `.env` file for actual configuration.

## Your API Credentials

### Dhan API
- **Client ID**: [Paste your Dhan Client ID here]
- **Access Token**: [Paste your Dhan Access Token here]

### Zerodha Kite API
- **API Key**: [Paste your Kite API Key here]
- **API Secret**: [Paste your Kite API Secret here]
- **Access Token**: [Paste your Kite Access Token here]

### Financial Modeling Prep (FMP)
- **API Key**: [Paste your FMP API Key here]

### Hugging Face
- **Token**: [Paste your Hugging Face Token here]
- **Space URL**: [Paste your Hugging Face Space URL here]

### Database (if applicable)
- **Database URL**: [Paste your database connection string here]

---

## Instructions

Since this is a private repository and you want to share your tokens:

1. **Paste your actual tokens** in the sections above, replacing the placeholder text
2. **Keep this file private** - ensure the repository remains private
3. **Create a .env file** using these tokens:
   - Copy `.env.template` to `.env`
   - Fill in the values from this file
   - The `.env` file won't be committed to git (it's in `.gitignore`)

## Alternative: Direct .env File

Instead of documenting tokens here, you can create a `.env` file directly:

```bash
cp .env.template .env
# Edit .env and add your tokens
```

The `.env` file will be ignored by git but will be available for your scripts to use.

## Note on Hugging Face Space

If you have secrets stored in a Hugging Face Space, you can either:
1. **Manually copy them here** for documentation
2. **Reference them in your code** if you have API access to pull them programmatically
3. **Use the Hugging Face Spaces API** to fetch secrets if your space has that configured

Unfortunately, I cannot directly connect to your Hugging Face Space to pull secrets, but you can easily copy them from your Space settings and paste them here.

## Security Reminder

Even in a private repository:
- Rotate keys regularly
- Monitor API usage
- Use read-only keys where possible
- Be cautious about who has repository access
