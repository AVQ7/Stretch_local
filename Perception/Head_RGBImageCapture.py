# import pyrealsense2 as rs
# import numpy as np
# import cv2
# # Initialize pipeline
# pipeline = rs.pipeline()

# # Configure the pipeline to stream depth and color data
# config = rs.config
# config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)  # Adjust resolution if necessary
# #config = rs.config()
# # config.enable_device(rs.camera_info.))  # Use serial number of the gripper camera

# # Start the pipeline
# pipeline.start(config)

# try:
#     # Wait for a coherent frame from the camera
#     frames = pipeline.wait_for_frames()
#     color_frame = frames.get_color_frame()

#     # Convert the color frame to numpy array
#     color_image = np.asanyarray(color_frame.get_data())

#     # Display the image using OpenCV
#     cv2.imshow("Captured Image", color_image)

#     # Save the image
#     cv2.imwrite('captured_image.png', color_image)
    
#     # Wait for a key press before closing the window
#     cv2.waitKey(0)
    
# finally:
#     # Stop the pipeline
#     pipeline.stop()

# # Release OpenCV windows
# cv2.destroyAllWindows()



import pyrealsense2 as rs
import numpy as np
import cv2

# Initialize pipeline
pipeline = rs.pipeline()

# Configure the pipeline to stream depth and color data
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)  # You can adjust resolution if needed

# (Optional) If you want to configure it for a specific camera by serial number:
# serial_number = 'Your_Gripper_Camera_Serial_Number'
# config.enable_device(serial_number)  # Uncomment and set the serial number if required

# Start the pipeline
pipeline.start(config)

try:
    # Wait for a coherent frame from the camera
    frames = pipeline.wait_for_frames()
    color_frame = frames.get_color_frame()

    if not color_frame:
        print("Error: No color frame received")
        exit(1)

    # Convert the color frame to numpy array
    color_image = np.asanyarray(color_frame.get_data())

    # Display the image using OpenCV
    cv2.imshow("Captured Image", color_image)

    # Save the image
    cv2.imwrite('captured_image.png', color_image)

    # Wait for a key press before closing the window
    cv2.waitKey(0)
    
finally:
    # Stop the pipeline
    pipeline.stop()

# Release OpenCV windows
cv2.destroyAllWindows()