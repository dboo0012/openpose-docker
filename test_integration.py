#!/usr/bin/env python3
"""
Test script to verify OpenPose integration with the backend.
This script now includes a full processing test.
"""
import sys
import traceback

# Import the new OpenPose test function
from test_openpose import run_openpose_on_image

def test_imports_and_processing():
    """Test all critical imports and run a full OpenPose processing test."""
    print("--- Testing Critical Imports ---")
    
    # Test PyTorch
    try:
        import torch
        print(f"✓ PyTorch: {torch.__version__}")
        print(f"✓ CUDA available: {torch.cuda.is_available()}")
        if torch.cuda.is_available():
            print(f"✓ CUDA device: {torch.cuda.get_device_name()}")
    except Exception as e:
        print(f"✗ PyTorch import failed: {e}")
    
    # Test OpenCV
    try:
        import cv2
        print(f"✓ OpenCV: {cv2.__version__}")
    except Exception as e:
        print(f"✗ OpenCV import failed: {e}")
    
    # Test NumPy
    try:
        import numpy as np
        print(f"✓ NumPy: {np.__version__}")
    except Exception as e:
        print(f"✗ NumPy import failed: {e}")
    
    print("\n--- Testing OpenPose Initialization ---")
    # Test OpenPose
    try:
        # Add OpenPose Python path
        sys.path.append('/openpose/build/python')
        from openpose import pyopenpose as op
        print("✓ OpenPose imported successfully")
        
        # Configure and start OpenPose
        params = {
            "model_folder": "/openpose/models/",
            "model_pose": "BODY_25",
            "net_resolution": "-1x368", # A good default for performance
            "number_people_max": 1, # Optimize for single person detection
            "disable_blending": True # Improves performance
        }
        opWrapper = op.WrapperPython()
        opWrapper.configure(params)
        opWrapper.start()
        print("✓ OpenPose wrapper initialized successfully")
        
        # --- NEW: RUN THE ACTUAL PROCESSING TEST ---
        run_openpose_on_image(opWrapper)
        
    except Exception as e:
        print(f"✗ OpenPose import/init failed: {e}")
        traceback.print_exc()
        
    # Test FastAPI
    try:
        from fastapi import FastAPI
        print("\n--- Testing FastAPI Import ---")
        print("✓ FastAPI imported successfully")
    except Exception as e:
        print(f"✗ FastAPI import failed: {e}")

if __name__ == "__main__":
    test_imports_and_processing()
    print("\nIntegration test completed!")
