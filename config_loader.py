"""
Configuration Loader for ATS-NSE-Stock-Suite

This module loads API credentials and configuration from environment variables.
It uses python-dotenv to load variables from a .env file.

Usage:
    from config_loader import config
    
    dhan_client_id = config.DHAN_CLIENT_ID
    kite_api_key = config.KITE_API_KEY
"""

import os
from pathlib import Path
from typing import Optional

# Try to import dotenv, provide helpful error if not installed
try:
    from dotenv import load_dotenv
except ImportError:
    print("Warning: python-dotenv not installed. Install it with: pip install python-dotenv")
    load_dotenv = None


class Config:
    """Configuration class that loads environment variables."""
    
    def __init__(self):
        """Initialize configuration by loading .env file if it exists."""
        if load_dotenv:
            # Load .env file from the project root
            env_path = Path(__file__).parent / '.env'
            if env_path.exists():
                load_dotenv(dotenv_path=env_path)
                print(f"Loaded environment variables from {env_path}")
            else:
                print(f"Warning: .env file not found at {env_path}")
                print("Create one by copying .env.template to .env and filling in your tokens")
        
        # Dhan API Configuration
        self.DHAN_CLIENT_ID: Optional[str] = os.getenv('DHAN_CLIENT_ID')
        self.DHAN_ACCESS_TOKEN: Optional[str] = os.getenv('DHAN_ACCESS_TOKEN')
        
        # Zerodha Kite API Configuration
        self.KITE_API_KEY: Optional[str] = os.getenv('KITE_API_KEY')
        self.KITE_API_SECRET: Optional[str] = os.getenv('KITE_API_SECRET')
        self.KITE_ACCESS_TOKEN: Optional[str] = os.getenv('KITE_ACCESS_TOKEN')
        
        # Financial Modeling Prep (FMP) API Configuration
        self.FMP_API_KEY: Optional[str] = os.getenv('FMP_API_KEY')
        
        # Hugging Face Configuration
        self.HUGGINGFACE_TOKEN: Optional[str] = os.getenv('HUGGINGFACE_TOKEN')
        self.HUGGINGFACE_SPACE_URL: Optional[str] = os.getenv('HUGGINGFACE_SPACE_URL')
        
        # Database Configuration
        self.DATABASE_URL: Optional[str] = os.getenv('DATABASE_URL')
        
        # Other Configuration
        self.DEBUG_MODE: bool = os.getenv('DEBUG_MODE', 'False').lower() == 'true'
        self.LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'INFO')
    
    def validate(self) -> bool:
        """
        Validate that required configuration variables are set.
        
        Returns:
            bool: True if all required variables are set, False otherwise
        """
        required_vars = []
        missing_vars = []
        
        # Add required variables based on your needs
        # Uncomment the ones you need:
        # required_vars.append(('DHAN_CLIENT_ID', self.DHAN_CLIENT_ID))
        # required_vars.append(('DHAN_ACCESS_TOKEN', self.DHAN_ACCESS_TOKEN))
        # required_vars.append(('KITE_API_KEY', self.KITE_API_KEY))
        # required_vars.append(('FMP_API_KEY', self.FMP_API_KEY))
        
        for var_name, var_value in required_vars:
            if not var_value:
                missing_vars.append(var_name)
        
        if missing_vars:
            print(f"Missing required environment variables: {', '.join(missing_vars)}")
            return False
        
        return True
    
    def __repr__(self) -> str:
        """Return a safe string representation of the config (without exposing secrets)."""
        return (
            f"Config("
            f"DHAN_CLIENT_ID={'***' if self.DHAN_CLIENT_ID else 'Not set'}, "
            f"KITE_API_KEY={'***' if self.KITE_API_KEY else 'Not set'}, "
            f"FMP_API_KEY={'***' if self.FMP_API_KEY else 'Not set'}, "
            f"HUGGINGFACE_TOKEN={'***' if self.HUGGINGFACE_TOKEN else 'Not set'}, "
            f"DEBUG_MODE={self.DEBUG_MODE}, "
            f"LOG_LEVEL={self.LOG_LEVEL}"
            f")"
        )


# Create a singleton instance
config = Config()


if __name__ == "__main__":
    """Test the configuration loader."""
    print("ATS-NSE-Stock-Suite Configuration Loader")
    print("=" * 50)
    print(config)
    print("\nValidation:", "PASSED" if config.validate() else "FAILED")
    print("\nTo fix missing variables:")
    print("1. Copy .env.template to .env")
    print("2. Fill in your API keys and tokens")
    print("3. Run this script again")
