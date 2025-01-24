import pyrealsense2 as rs
import numpy as np
import cv2

# Gripper Camera Serial Number
gripper_camera_serial_number = '130322274287'

# Initialize pipeline
pipeline = rs.pipeline()

# Configure the pipeline to stream color data from the gripper camera
config = rs.config()
config.enable_device(gripper_camera_serial_number)  # Enable the gripper camera using its serial number
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)  # Adjust resolution if needed

# Start the pipeline
pipeline.start(config)

try:
    # Wait for a coherent frame from the gripper camera
    frames = pipeline.wait_for_frames()
    color_frame = frames.get_color_frame()

    if not color_frame:
        print("Error: No color frame received from the gripper camera")
        exit(1)

    # Convert the color frame to numpy array
    color_image = np.asanyarray(color_frame.get_data())

    # Display the image using OpenCV
    cv2.imshow("Captured Image from Gripper Camera", color_image)

    # Save the image
    cv2.imwrite('gripper_captured_image.png', color_image)

    # Wait for a key press before closing the window
    cv2.waitKey(0)

finally:
    # Stop the pipeline
    pipeline.stop()

# Release OpenCV windows
cv2.destroyAllWindows()