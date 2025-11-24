# GitHub Copilot Instructions for ATS-NSE-Stock-Suite

## Repository Overview

This is an NSE (National Stock Exchange) Stock Market Analysis Suite with Live Data Integration, Excel Analytics, and VBA Automation capabilities. The project provides tools for fetching stock market data, analyzing it, and exporting results to Excel for further analysis or automation.

**Developer**: Mandar Bahadarpurkar  
**Language**: Python 3.12+  
**Status**: Production-ready with comprehensive mock data support

## Project Purpose

ATS-NSE-Stock-Suite enables users to:
- Fetch live stock market data from multiple APIs (Dhan, Zerodha Kite, FMP, Yahoo Finance, Alpha Vantage)
- Generate realistic mock data for development and testing without API keys
- Analyze stock market data including historical trends, portfolio tracking, and market indices
- Export data to Excel for reporting and VBA automation
- Manage API credentials securely using environment variables

## Project Structure

```
ATS-NSE-Stock-Suite/
├── .github/                  # GitHub configuration (Copilot instructions, etc.)
├── .env.template            # Template for environment variables (copy to .env)
├── .gitignore              # Git ignore rules (includes .env for security)
├── config_loader.py        # Configuration management and API credential loading
├── nse_data_fetcher.py     # Live API data fetcher (Yahoo Finance, Alpha Vantage)
├── mock_nse_data.py        # Mock data generator for offline development
├── excel_integration.py    # Excel export functionality with formatting
├── demo_app.py            # Complete demonstration application
├── example_usage.py        # Usage examples for configuration
├── test_integration.py     # Integration test suite (run before deployment)
├── setup_production.py     # Production setup utilities
├── requirements.txt        # Python dependencies
├── README.md              # Main documentation
├── CONFIG.md              # Detailed API configuration guide
├── QUICKSTART.md          # Quick start guide
├── PROJECT_SUMMARY.md     # Project status and deliverables
├── INSTALLATION.md        # Detailed installation instructions
├── HUGGINGFACE_GUIDE.md   # Hugging Face integration guide
├── SECRETS.md             # Token documentation template (private repo)
└── DELIVERY_SUMMARY.md    # Delivery and milestone tracking
```

## How to Build and Test

### Initial Setup
```bash
# Install dependencies
pip install -r requirements.txt

# (Optional) Create .env file from template for API keys
cp .env.template .env
# Edit .env with your API credentials if needed
```

### Running Tests
```bash
# Run integration tests (ALL must pass before committing)
python test_integration.py

# All tests must pass for the application to be considered functional
# The test suite will report the number of passed/total tests
```

### Running the Application
```bash
# Run complete demo (works without API keys using mock data)
python demo_app.py

# Run specific examples
python example_usage.py
```

### Testing Changes
When making changes to the codebase:
1. Run `python test_integration.py` to verify core functionality
2. If you modify data fetching: Test with mock data first
3. If you modify Excel exports: Check generated .xlsx files manually
4. If you modify configuration: Verify .env template is updated

## Coding Standards and Conventions

### Python Style
- **Follow PEP 8** for code formatting
- Use **descriptive variable names** (e.g., `stock_quote` not `sq`)
- Add **docstrings** to all functions and classes explaining purpose, parameters, and return values
- Use **type hints** where appropriate for clarity
- Keep functions **focused and single-purpose**

### Code Organization
- Each module has a specific purpose (data fetching, Excel export, mock data, etc.)
- Keep business logic separate from presentation/export logic
- Mock data should mirror the structure of real API responses
- Configuration should be externalized to .env files

### Error Handling
- Use try-except blocks for API calls and file operations
- Provide **meaningful error messages** to users
- Log errors appropriately (check existing patterns in nse_data_fetcher.py)
- Gracefully handle missing API keys by falling back to mock data or providing clear instructions

### Security Best Practices
- **NEVER commit API keys, tokens, or credentials** to the repository
- Always use environment variables via `python-dotenv` for sensitive data
- The `.env` file is in `.gitignore` - keep it that way
- Document required environment variables in `.env.template`
- Rotate API keys regularly and monitor for unusual usage

### Comments and Documentation
- Add comments for complex logic or non-obvious decisions
- Update README.md if adding new features or changing workflows
- Update CONFIG.md if adding new API integrations
- Keep docstrings up to date with code changes

## Dependencies and APIs

### Core Dependencies (Required)
See `requirements.txt` for exact versions. Core dependencies include:
- `python-dotenv` - Environment variable management
- `requests` - HTTP requests for API calls
- `pandas` - Data processing and manipulation
- `numpy` - Numerical operations
- `openpyxl` - Excel file generation
- `python-dateutil` - Date utilities

### API Integrations
The project supports multiple data sources:

1. **Yahoo Finance** (Free, no key needed)
   - Used for: Real-time quotes and historical data
   - Module: `nse_data_fetcher.py`
   - No configuration required

2. **Alpha Vantage** (Free tier available)
   - Used for: Alternative data source
   - Requires: `ALPHA_VANTAGE_API_KEY` in .env
   - See CONFIG.md for setup

3. **Dhan API** (Premium)
   - Requires: `DHAN_CLIENT_ID`, `DHAN_ACCESS_TOKEN`
   - Module: Can be integrated via config_loader.py

4. **Zerodha Kite** (Premium)
   - Requires: `KITE_API_KEY`, `KITE_API_SECRET`, `KITE_ACCESS_TOKEN`
   - Module: Can be integrated via config_loader.py

5. **Financial Modeling Prep** (Premium)
   - Requires: `FMP_API_KEY`
   - Module: Can be integrated via config_loader.py

6. **Mock Data** (Default, no keys needed)
   - Module: `mock_nse_data.py`
   - Generates realistic stock data for development
   - Use this for testing to avoid API rate limits

### Adding New Dependencies
When adding a new dependency:
1. Add it to `requirements.txt` with a pinned version
2. Document why it's needed (add comment in requirements.txt)
3. Update README.md if it affects user setup
4. Test that the application works with and without the new dependency

## Key Features and Modules

### 1. Mock Data Generation (`mock_nse_data.py`)
- Generates realistic NSE stock data without API calls
- Supports 20+ major NSE stocks (RELIANCE, TCS, INFY, etc.)
- Includes volatility simulation and price movements
- Use for development, testing, and demonstrations
- Pattern: All methods return dictionaries with consistent structure

### 2. Live Data Fetching (`nse_data_fetcher.py`)
- Integrates with Yahoo Finance (primary) and Alpha Vantage
- Handles API rate limiting and errors gracefully
- Returns data in the same format as mock data for consistency
- Pattern: Falls back to mock data if API calls fail

### 3. Excel Integration (`excel_integration.py`)
- Exports stock quotes, historical data, and portfolios to Excel
- Applies formatting (headers, number formats, column widths)
- Supports multiple export formats:
  - Stock quotes: Single-row format
  - Historical data: Time-series format with metadata
  - Portfolio: Multi-stock tracking with calculations
  - Watchlist: Template for user customization
- Pattern: All export methods return the filepath of the created file

### 4. Configuration Management (`config_loader.py`)
- Loads environment variables from .env file
- Provides default values for missing configuration
- Validates configuration and provides helpful error messages
- Pattern: Use `config.VARIABLE_NAME` to access configuration

### 5. Demonstration App (`demo_app.py`)
- Shows all features in action with no setup required
- Generates sample Excel files
- Great starting point for understanding the codebase
- Pattern: Self-contained, works with mock data only

## Contribution Guidelines

### Making Changes
1. **Before coding**: Read relevant documentation (README.md, CONFIG.md)
2. **Small changes**: Make minimal, focused modifications
3. **Test thoroughly**: Run `python test_integration.py` after changes
4. **Document changes**: Update docs if adding features or changing behavior
5. **Check git status**: Ensure no sensitive files (.env) are staged

### Pull Request Guidelines
- Keep PRs focused on a single feature or fix
- Include a clear description of what changed and why
- Ensure all tests pass before requesting review
- Update documentation in the same PR if behavior changes
- Add usage examples for new features

### Testing Checklist
Before submitting code:
- [ ] All integration tests pass (`python test_integration.py`)
- [ ] Mock data generation works correctly
- [ ] Excel exports generate valid .xlsx files
- [ ] Configuration loading works with .env
- [ ] No API keys or sensitive data in commits
- [ ] Code follows PEP 8 style guidelines
- [ ] Docstrings are present and accurate
- [ ] README.md is updated if needed

## Common Tasks

### Adding a New API Integration
1. Add required credentials to `.env.template` with placeholder values
2. Update `config_loader.py` to load the new credentials
3. Create or update a fetcher class in `nse_data_fetcher.py`
4. Ensure data format matches mock data structure
5. Add error handling and fallback to mock data
6. Update `CONFIG.md` with setup instructions
7. Test with both valid and invalid API keys

### Adding a New Stock Symbol
1. Add the symbol to `STOCK_INFO` dictionary in `mock_nse_data.py`
2. Include symbol, company name, sector, and typical price range
3. Test that mock data generation works for the new symbol
4. Update documentation or examples if relevant

### Adding a New Excel Export Format
1. Add a new method to `ExcelExporter` class in `excel_integration.py`
2. Follow existing patterns for worksheet creation and formatting
3. Return the filepath of the generated file
4. Add example usage to `demo_app.py`
5. Test the generated Excel file manually

### Modifying Tests
- Tests are in `test_integration.py`
- Each test function should have a clear, descriptive name
- Tests should be independent (no shared state)
- Add new tests for new features
- Ensure test output is clear and actionable

## Important Notes for GitHub Copilot

### API Key Usage
- When generating code that uses APIs, ALWAYS provide a mock data fallback
- Check for API key presence before making API calls
- Guide users to use mock data for development/testing

### Excel Operations
- Use `openpyxl` for all Excel operations (already a dependency)
- Follow existing formatting patterns in `excel_integration.py`
- Always set column widths for readability
- Apply number formatting for prices and percentages

### Data Structure Consistency
- Stock quotes should include: symbol, price, change, change_percent, volume, timestamp
- Historical data should be a list of OHLC dictionaries with date, open, high, low, close, volume
- Portfolio data should include symbol, quantity, current_price, total_value

### Error Messages
- Be specific about what went wrong
- Provide actionable next steps for users
- Reference documentation files (CONFIG.md, README.md) when appropriate

### Security Awareness
- Never suggest hardcoding API keys
- Always use environment variables for sensitive data
- Remind users to check `.gitignore` includes `.env`
- Validate that `.env.template` is updated for new credentials

## Questions to Ask Users

When assigned a task, consider asking:
- "Should this work with mock data, live APIs, or both?"
- "Do you want this exported to Excel?"
- "Should I update the documentation for this change?"
- "Do you have API keys configured, or should I use mock data?"
- "Should this be added to the demo app or integration tests?"

## Success Criteria

A task is complete when:
- [ ] All integration tests pass
- [ ] Code follows established patterns and conventions
- [ ] Documentation is updated appropriately
- [ ] No security issues introduced
- [ ] Excel exports (if applicable) are manually verified
- [ ] Mock data support is maintained
- [ ] Error handling is appropriate and helpful
