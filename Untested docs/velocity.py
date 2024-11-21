import stretch_body.robot

# you could set velocity commands to any part of the robots macro-movements
r = stretch_body.robot.Robot() #create an instance of the robot object

did_startup = r.startup()
print(f'Robot connected to hardware: {did_startup}')


is_homed = r.is_homed()
print(f'Robot is homed: {is_homed}')

r.end_of_arm.get_joint('wrist_yaw').set_velocity(0.1) # rotate CCW at 0.1 rad/s
#for the base of the robot, the set_velocity api can take 2 parameters
r.base.set_velocity(2, 2) # follow a circular path when tested the robot tdoes not follow circular path 
r.push_command()
r.end_of_arm.trajectory.add(t_s=10.0, x_m=0.5, v_m=0.4) # 20 second trajectory extending & retracting the arm
r.follow_trajectory()

r.push_command()