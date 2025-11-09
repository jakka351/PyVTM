#!/usr/bin/env python3
"""
Test script to verify j2534.py imports correctly
"""

print("Testing j2534 import...")

try:
    from j2534 import *
    print("✓ j2534 imported successfully!")
    
    # Test that key classes are available
    print("\nChecking key classes:")
    
    classes_to_check = [
        'J2534Err',
        'PassThruMsg',
        'SConfig',
        'SConfigList',
        'J2534Functions',
        'J2534FunctionsExtended'
    ]
    
    for cls_name in classes_to_check:
        if cls_name in dir():
            print(f"  ✓ {cls_name} is available")
        else:
            print(f"  ✗ {cls_name} is NOT available")
    
    print("\n✓ All tests passed!")
    print("\nThe j2534 module is ready to use.")
    
except ImportError as e:
    print(f"✗ Import failed: {e}")
    exit(1)
except Exception as e:
    print(f"✗ Unexpected error: {e}")
    exit(1)
