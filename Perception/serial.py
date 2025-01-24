import pyrealsense2 as rs

# Initialize the context for all connected devices
context = rs.context()

# Loop through all connected devices and print their serial numbers
for device in context.devices:
    print(f"Device name: {device.get_info(rs.camera_info.name)}")
    print(f"Serial number: {device.get_info(rs.camera_info.serial_number)}")