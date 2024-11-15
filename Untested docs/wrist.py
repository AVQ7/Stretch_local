import stretch_body.robot
# methods for the end of the robot arm aka the hand, 
# here's a link to an image to help you visualize the joint:
# https://media.licdn.com/dms/image/v2/D5612AQF_PnTPfeXk8g/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1695722959735?e=2147483647&v=beta&t=C3aPEcORJ4MYjpFe38SZiO1_VGTfXvK7IbfwN33OwJo
r = stretch_body.robot.Robot() #create an instane of the robot object

# prints the different joints in the arm
print(f'Wrist joints: {r.end_of_arm.joints}') # ['wrist_yaw', 'wrist_pitch', 'wrist_roll', 'stretch_gripper']

#Note: none of these actions are queried, they execute immediatly without the r.push_command() command
# . method move_to("name of joint", radians). positive radian means clockwise 
r.end_of_arm.move_to('wrist_yaw', 1.57) # wrist spins about z-axis

r.end_of_arm.move_to('wrist_roll', 1.57) # wrist spins about x-axis, 

r.end_of_arm.move_to('wrist_pitch', 1.57) #  wrist spins about y-axis

# the following is for the gripper attached to the arm. -100(max closed) to 100(max open)
r.end_of_arm.move_to('stretch_gripper', 100)

# the following is to fetch the current state of the joint 
print(r.end_of_arm.get_joint('wrist_yaw').status['pos']) # radians

# prints a dictionary with four keys: "collision", "user", "hard", and "current"
# each key is assigned a tuple (lower_bound, upper_bound) in radians 
print(r.end_of_arm.get_joint('wrist_yaw').soft_motion_limits['hard']) 
# "collision" is used by Stretch Body's self collision avoidance algorithm to set software limits on the joint.
# "user" is used by you, the user, to set application specific software joint limits. "hard" is the hardware limits of the joint. 
# And "current" is the aggregate of the previous three limits into the final limits enforced by the software.