#!/usr/bin/env python3
"""
ML Dashboard Startup Script
Simple script to run the ML Dashboard with proper configuration
"""

import os
import sys
import subprocess
import webbrowser
from threading import Timer

def open_browser():
    """Open browser after a short delay"""
    webbrowser.open('http://localhost:5000')

def main():
    """Main startup function"""
    print("=" * 60)
    print("🤖 Machine Learning Dashboard")
    print("=" * 60)
    print("Starting the ML Dashboard...")
    print("This will open your browser automatically in a few seconds.")
    print("If it doesn't open, navigate to: http://localhost:5000")
    print("=" * 60)
    print()
    
    # Check if virtual environment is activated
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Virtual environment detected")
    else:
        print("⚠️  Warning: No virtual environment detected")
        print("   Consider using a virtual environment for better dependency management")
        print()
    
    # Check if required packages are installed
    try:
        import flask
        import tensorflow
        import numpy
        import pandas
        import sklearn
        print("✅ All required packages are installed")
    except ImportError as e:
        print(f"❌ Missing required package: {e}")
        print("Please run: pip install -r requirements.txt")
        return
    
    print()
    print("🚀 Starting Flask application...")
    print("Press Ctrl+C to stop the server")
    print()
    
    # Open browser after 2 seconds
    Timer(2.0, open_browser).start()
    
    # Start the Flask app
    try:
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n👋 Shutting down ML Dashboard...")
        print("Thank you for using the ML Dashboard!")
    except Exception as e:
        print(f"❌ Error starting the application: {e}")
        print("Please check the error message above and try again.")

if __name__ == '__main__':
    main()
