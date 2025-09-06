#!/usr/bin/env python3
"""
ML Dashboard Installation Test
This script tests if all required packages are properly installed
"""

import sys
import importlib

def test_package(package_name, import_name=None):
    """Test if a package can be imported"""
    if import_name is None:
        import_name = package_name
    
    try:
        module = importlib.import_module(import_name)
        version = getattr(module, '__version__', 'Unknown')
        print(f"✅ {package_name}: {version}")
        return True
    except ImportError:
        print(f"❌ {package_name}: Not installed")
        return False

def main():
    """Main test function"""
    print("=" * 60)
    print("🧪 ML Dashboard Installation Test")
    print("=" * 60)
    print()
    
    # Required packages
    packages = [
        ('Flask', 'flask'),
        ('Flask-CORS', 'flask_cors'),
        ('TensorFlow', 'tensorflow'),
        ('NumPy', 'numpy'),
        ('Pandas', 'pandas'),
        ('Scikit-learn', 'sklearn'),
        ('Matplotlib', 'matplotlib'),
        ('Seaborn', 'seaborn'),
        ('Plotly', 'plotly'),
    ]
    
    print("Testing required packages...")
    print("-" * 40)
    
    all_installed = True
    for package_name, import_name in packages:
        if not test_package(package_name, import_name):
            all_installed = False
    
    print()
    print("=" * 60)
    
    if all_installed:
        print("🎉 All packages are installed correctly!")
        print("You can now run the ML Dashboard using:")
        print("  python app.py")
        print("  or")
        print("  python run.py")
        print("  or")
        print("  start_dashboard.bat (Windows)")
    else:
        print("❌ Some packages are missing!")
        print("Please install missing packages using:")
        print("  pip install -r requirements.txt")
        print()
        print("If you're using a virtual environment, make sure it's activated:")
        print("  venv\\Scripts\\activate (Windows)")
        print("  source venv/bin/activate (macOS/Linux)")
    
    print("=" * 60)
    
    # Test TensorFlow functionality
    if all_installed:
        print()
        print("Testing TensorFlow functionality...")
        try:
            import tensorflow as tf
            print(f"✅ TensorFlow version: {tf.__version__}")
            print(f"✅ GPU available: {tf.config.list_physical_devices('GPU')}")
            
            # Test basic TensorFlow operations
            a = tf.constant([1, 2, 3])
            b = tf.constant([4, 5, 6])
            c = tf.add(a, b)
            print(f"✅ Basic operations working: {c.numpy()}")
            
        except Exception as e:
            print(f"❌ TensorFlow test failed: {e}")
            all_installed = False
    
    return all_installed

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
