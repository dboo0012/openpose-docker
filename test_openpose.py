import sys
import cv2

# This path is added by the main script, but it's good practice to note it's needed
sys.path.append('/openpose/build/python')
try:
    from openpose import pyopenpose as op
except ImportError as e:
    print(f"Error: OpenPose library could not be found. {e}")
    sys.exit(-1)

def run_openpose_on_image(op_wrapper):
    """
    Initializes OpenPose, processes a sample image, and prints the results.

    Args:
        op_wrapper: The initialized op.WrapperPython object from the main script.

    Returns:
        True if keypoints are detected, False otherwise.
    """
    print("--- Running OpenPose processing on a sample image ---")
    try:
        # 1. Read the sample image
        image_path = "/openpose/examples/media/COCO_val2014_000000000192.jpg"
        image_to_process = cv2.imread(image_path)
        if image_to_process is None:
            print(f"✗ Could not read image from path: {image_path}")
            return False
        
        print(f"✓ Successfully loaded image: {image_path}")

        # 2. Create a Datum object and process the image
        datum = op.Datum()
        datum.cvInputData = image_to_process
        op_wrapper.emplaceAndPop(op.VectorDatum([datum]))

        # 3. Check and print the results
        if datum.poseKeypoints is not None:
            print(f"✓ OK: Keypoints detected. Shape: {datum.poseKeypoints.shape}")
            # The shape (1, 25, 3) means: 1 person, 25 keypoints, 3 values (x, y, confidence)
            print("--- Detected Keypoints (x, y, confidence) ---")
            print(datum.poseKeypoints)
            return True
        else:
            print("✗ FAILED: No keypoints detected in the image.")
            return False

    except Exception as e:
        print(f"✗ An exception occurred during OpenPose processing: {e}")
        return False
