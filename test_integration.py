#!/usr/bin/env python3
"""
Test script to verify OpenPose integration with the backend
"""
import sys
import traceback

def test_imports():
    """Test all critical imports"""
    print("Testing imports...")
    
    try:
        import torch
        print(f"✓ PyTorch: {torch.__version__}")
        print(f"✓ CUDA available: {torch.cuda.is_available()}")
        if torch.cuda.is_available():
            print(f"✓ CUDA device: {torch.cuda.get_device_name()}")
    except Exception as e:
        print(f"✗ PyTorch import failed: {e}")
        
    try:
        import cv2
        print(f"✓ OpenCV: {cv2.__version__}")
    except Exception as e:
        print(f"✗ OpenCV import failed: {e}")
        
    try:
        import numpy as np
        print(f"✓ NumPy: {np.__version__}")
    except Exception as e:
        print(f"✗ NumPy import failed: {e}")
        
    try:
        # Add OpenPose Python path
        sys.path.append('/openpose/build/python')
        import openpose as op
        print("✓ OpenPose imported successfully")
        
        # Test OpenPose initialization
        params = dict()
        params["model_folder"] = "/openpose/models/"
        opWrapper = op.WrapperPython()
        opWrapper.configure(params)
        opWrapper.start()
        print("✓ OpenPose wrapper initialized successfully")
        
    except Exception as e:
        print(f"✗ OpenPose import/init failed: {e}")
        traceback.print_exc()
        
    try:
        from fastapi import FastAPI
        print("✓ FastAPI imported successfully")
    except Exception as e:
        print(f"✗ FastAPI import failed: {e}")

if __name__ == "__main__":
    test_imports()
    print("\nTest completed!")
