import pyrealsense2 as rs
import numpy as np
import cv2

# Serial numbers for the cameras
serial_head = "239722071443"  # Replace with your D435i serial number
serial_gripper = "130322274287"  # Replace with your D405 serial number

# Initialize pipelines for both cameras
pipeline_head = rs.pipeline()
pipeline_gripper = rs.pipeline()

# Configure the streams for the head camera (D435i)
config_head = rs.config()
config_head.enable_device(serial_head)
config_head.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)  # Adjust resolution and FPS as needed

# Configure the streams for the gripper camera (D405)
config_gripper = rs.config()
config_gripper.enable_device(serial_gripper)
config_gripper.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)  # Adjust resolution and FPS as needed

try:
    # Start pipelines
    pipeline_head.start(config_head)
    pipeline_gripper.start(config_gripper)
    print("Both cameras initialized successfully. Press 'q' to quit.")

    while True:
        # Get frames from both cameras
        frames_head = pipeline_head.wait_for_frames()
        frames_gripper = pipeline_gripper.wait_for_frames()

        # Extract color frames
        color_frame_head = frames_head.get_color_frame()
        color_frame_gripper = frames_gripper.get_color_frame()

        if color_frame_head and color_frame_gripper:
            # Convert frames to numpy arrays
            color_image_head = np.asanyarray(color_frame_head.get_data())
            color_image_gripper = np.asanyarray(color_frame_gripper.get_data())

            # Display the frames
            cv2.imshow("Head Camera (D435i)", color_image_head)
            cv2.imshow("Gripper Camera (D405)", color_image_gripper)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

finally:
    # Stop both pipelines
   # pipeline_head.stop()
    pipeline_gripper.stop()
    pipeline_head.stop()
    cv2.destroyAllWindows()