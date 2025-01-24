
from stretch_body.robot import Robot
import pyrealsense2 as rs
import cv2
import time
import numpy as np

# #collecting data from the cmeras aboard stretch.
# cam = rs.pipeline()
# # cam.start()
# # cam.stop()
# profile = cam.start()
# print(profile.get_device().get_info()) # "D435if"
# config = rs.config()
# config.enable_device(d405_info['serial_number'])
# width, height, fps = 640, 480, 15
# config.enable_stream(rs.stream.depth, width, height, rs.format.z16, fps)
# config.enable_stream(rs.stream.color, width, height, rs.format.bgr8, fps)
# profile = cam.start(config)

# Initialize pipeline

# Initialize robot and camera
robot = Robot()
robot.startup()

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)
pipeline.start(config)

try:
    with open("robot_data_log.csv", "w") as log_file:
        log_file.write("timestamp,base_x,base_y,base_theta,lift_pos,arm_pos,wrist_yaw_pos\n")
        while True:
            # Get position data
            base_pose = robot.base.status['x'], robot.base.status['y'], robot.base.status['theta']
            joint_positions = {
                'lift': robot.lift.status['pos'],
                'arm': robot.arm.status['pos'],
                'wrist': robot.end_of_arm.status['wrist_yaw']['pos']
            }

            # Get camera frame
            frames = pipeline.wait_for_frames()
            color_frame = frames.get_color_frame()
            if not color_frame:
                continue

            color_image = np.asanyarray(color_frame.get_data())
            cv2.imshow('Camera View', color_image)

            # Save data
            timestamp = time.time()
            log_file.write(f"{timestamp},{base_pose[0]},{base_pose[1]},{base_pose[2]},"
                           f"{joint_positions['lift']},{joint_positions['arm']},{joint_positions['wrist']}\n")

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
finally:
    robot.stop()
    pipeline.stop()
    cv2.destroyAllWindows()