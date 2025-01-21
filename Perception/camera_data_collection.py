import pyrealsense2 as rs

#collecting data from the cmeras aboard stretch.
cam = rs.pipeline()
# cam.start()
# cam.stop()
profile = cam.start()
print(profile.get_device().get_info()) # "D435if"
config = rs.config()
config.enable_device(d405_info['serial_number'])
width, height, fps = 640, 480, 15
config.enable_stream(rs.stream.depth, width, height, rs.format.z16, fps)
config.enable_stream(rs.stream.color, width, height, rs.format.bgr8, fps)
profile = cam.start(config)