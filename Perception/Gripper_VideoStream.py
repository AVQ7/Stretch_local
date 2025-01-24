import pyrealsense2 as rs
import numpy as np
import cv2

# Gripper camera serial number (D405)
serial_gripper = "130322274287"  # Replace with your actual D405 serial number

# Initialize the pipeline for the gripper camera
pipeline_gripper = rs.pipeline()

# Configure the stream for the gripper camera
config_gripper = rs.config()
config_gripper.enable_device(serial_gripper)
config_gripper.enable_stream(rs.stream.color)

try:
    # Start the pipeline
    pipeline_gripper.start(config_gripper)
    print("Gripper camera initialized successfully.")

    # Stream from the gripper camera
    while True:
        frames_gripper = pipeline_gripper.wait_for_frames()
        color_frame_gripper = frames_gripper.get_color_frame()

        if color_frame_gripper:
            color_image_gripper = np.asanyarray(color_frame_gripper.get_data())
            cv2.imshow("Gripper Camera (D405)", color_image_gripper)

        # Press 'q' to quit the stream
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
finally:
    pipeline_gripper.stop()
    cv2.destroyAllWindows()