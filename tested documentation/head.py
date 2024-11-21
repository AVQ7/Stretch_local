import stretch_body.robot

r = stretch_body.robot.Robot() #always create robot object

did_startup = r.startup()
print(f'Robot connected to hardware: {did_startup}')


is_homed = r.is_homed()
print(f'Robot is homed: {is_homed}')
#.head is an accessible attribute of the robot object, has 2 joints: Pan & tilt
# the head is controlled by dynamixel servos

print(r.head)

# the api for the head is .move_to("joint_name", pos)
# executes immediatly without r.push_command()
r.head.move_to('head_pan', -3) # -4.04 rad to 1.73 rad
r.head.move_to('head_tilt', 0.49) # (-2.02 to 0.49 rad) -2 tilts all the way up, 0.49 tilts down

# Check HEAD POSITION, status dictionary is under get_joint(name) method 
print(f'Head joints: {r.head.joints}') # prints all joints
print(r.head.get_joint('head_pan').status['pos'] ) # position of specific joint radians

# for JOINT CONSTRAINTS, check the soft_motion_limits dictionary
# this is a dictionary with 4 keys that each map to a tuple (lower_bound, upper_bound)
# the 4 keys are "collision", "user", "hard", and "current"
#"collision" is used by Stretch's self collision avoidance algorithm to set
#"user" is set by the user,for application specific software joint limits.
# "hard" is the hardware limits of the joint.
#"current" is the aggregate of the previous three limits, it's the one actually enforced by the software
print(r.head.get_joint('head_pan').soft_motion_limits['hard']) # (lower bound in meters, upper bound in meters)
print(r.head.get_joint('head_tilt').soft_motion_limits['current'])

#VELOCITY COMMANDS, use set_velocity(vel) API
r.head.get_joint('head_pan').set_velocity(0.05) # rotational velocity in this case

#TRAJECTORY SETTING & TRACKING
# for the head/wrist, the trajectory attribute is an instance of stretch_body.trajectories.RevoluteTrajectory
# trajectory attribute is important as it helps the joints sync up and
# coordinate for smooth multi-dimentional movement

#This line pauses the execution of the code for 2 seconds
r.time.sleep(2.0) 

# safety measure that halts any robot movement immediatly 
#r.stop() 