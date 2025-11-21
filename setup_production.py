#!/usr/bin/env python3
"""
Production Setup Script for ATS-NSE-Stock-Suite
================================================

This script helps set up the production environment for the NSE Stock Suite.
It checks dependencies, creates configuration files, and verifies the installation.

Run this script after extracting the package:
    python setup_production.py

Author: Mandar Bahadarpurkar
"""

import sys
import os
import subprocess
from pathlib import Path


def print_header(text):
    """Print formatted header."""
    print("\n" + "=" * 80)
    print(f"  {text}")
    print("=" * 80 + "\n")


def print_section(text):
    """Print formatted section."""
    print(f"\n{text}")
    print("-" * 80)


def check_python_version():
    """Check if Python version is compatible."""
    print_section("1. Checking Python Version")
    
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        return False
    
    print("✅ Python version is compatible")
    return True


def check_pip():
    """Check if pip is available."""
    print_section("2. Checking pip")
    
    try:
        result = subprocess.run(['pip3', '--version'], 
                              capture_output=True, text=True, check=True)
        print(f"pip version: {result.stdout.strip()}")
        print("✅ pip is available")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ pip is not available")
        print("Please install pip: https://pip.pypa.io/en/stable/installation/")
        return False


def install_dependencies():
    """Install required Python packages."""
    print_section("3. Installing Dependencies")
    
    requirements_file = Path(__file__).parent / 'requirements.txt'
    
    if not requirements_file.exists():
        print("❌ requirements.txt not found")
        return False
    
    print("Installing packages from requirements.txt...")
    try:
        result = subprocess.run(['pip3', 'install', '-r', str(requirements_file)],
                              capture_output=True, text=True, check=True)
        print("✅ All dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        print(e.stderr)
        return False


def create_env_file():
    """Create .env file from template if it doesn't exist."""
    print_section("4. Setting Up Configuration")
    
    env_file = Path(__file__).parent / '.env'
    template_file = Path(__file__).parent / '.env.template'
    
    if env_file.exists():
        print("ℹ️  .env file already exists")
        response = input("Do you want to overwrite it? (y/N): ").strip().lower()
        if response != 'y':
            print("✅ Keeping existing .env file")
            return True
    
    if not template_file.exists():
        print("❌ .env.template not found")
        return False
    
    try:
        with open(template_file, 'r') as src:
            content = src.read()
        
        with open(env_file, 'w') as dst:
            dst.write(content)
        
        print("✅ Created .env file from template")
        print("\nNOTE: Edit .env to add your API keys for live data")
        print("      The application works without API keys using mock data")
        return True
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")
        return False


def run_tests():
    """Run integration tests."""
    print_section("5. Running Tests")
    
    test_file = Path(__file__).parent / 'test_integration.py'
    
    if not test_file.exists():
        print("⚠️  test_integration.py not found, skipping tests")
        return True
    
    print("Running integration tests...")
    try:
        result = subprocess.run(['python3', str(test_file)],
                              capture_output=True, text=True)
        
        # Check if all tests passed
        if "Tests passed: 6/6" in result.stdout:
            print("✅ All tests passed (6/6)")
            return True
        else:
            print("⚠️  Some tests failed")
            print(result.stdout)
            return False
    except Exception as e:
        print(f"⚠️  Error running tests: {e}")
        return False


def verify_files():
    """Verify all required files are present."""
    print_section("6. Verifying Files")
    
    required_files = [
        'nse_data_fetcher.py',
        'mock_nse_data.py',
        'excel_integration.py',
        'demo_app.py',
        'config_loader.py',
        'requirements.txt',
        'README.md',
        'QUICKSTART.md'
    ]
    
    base_path = Path(__file__).parent
    all_present = True
    
    for filename in required_files:
        filepath = base_path / filename
        if filepath.exists():
            print(f"✅ {filename}")
        else:
            print(f"❌ {filename} not found")
            all_present = False
    
    return all_present


def print_next_steps():
    """Print next steps for the user."""
    print_header("Setup Complete!")
    
    print("Your ATS-NSE-Stock-Suite is ready to use!\n")
    
    print("Next Steps:")
    print("-" * 80)
    print("1. Run the demo application:")
    print("   python demo_app.py")
    print()
    print("2. (Optional) Configure API keys for live data:")
    print("   - Edit .env file with your API credentials")
    print("   - See CONFIG.md for detailed setup instructions")
    print()
    print("3. Explore the documentation:")
    print("   - README.md - Main documentation")
    print("   - QUICKSTART.md - Quick start guide")
    print("   - PROJECT_SUMMARY.md - Project overview")
    print()
    print("4. Start using the application:")
    print("   from mock_nse_data import MockNSEData")
    print("   mock = MockNSEData()")
    print("   quote = mock.get_stock_quote('RELIANCE')")
    print()
    print("=" * 80)
    print("Happy stock analysis! 📈")
    print("=" * 80)


def main():
    """Main setup function."""
    print_header("ATS-NSE-Stock-Suite - Production Setup")
    
    print("This script will set up your production environment.")
    print("Please wait while we check dependencies and configure the system...\n")
    
    # Run all setup steps
    steps = [
        ("Python version", check_python_version),
        ("pip availability", check_pip),
        ("Dependencies", install_dependencies),
        ("Configuration", create_env_file),
        ("Tests", run_tests),
        ("Files", verify_files),
    ]
    
    results = []
    for step_name, step_func in steps:
        try:
            result = step_func()
            results.append(result)
        except Exception as e:
            print(f"❌ Unexpected error in {step_name}: {e}")
            results.append(False)
    
    # Summary
    print_section("Setup Summary")
    passed = sum(results)
    total = len(results)
    
    print(f"Steps completed: {passed}/{total}\n")
    
    if passed == total:
        print("🎉 Production setup completed successfully!")
        print_next_steps()
        return 0
    else:
        print("⚠️  Setup completed with warnings")
        print("The application may still work, but some features might be limited.")
        print("\nPlease review the errors above and:")
        print("1. Install missing dependencies manually")
        print("2. Check system requirements in README.md")
        print("3. Contact support if issues persist")
        return 1


if __name__ == "__main__":
    sys.exit(main())
