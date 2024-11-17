import stretch_body.robot

# you could set velocity commands to any part of the robots macro-movements
r = stretch_body.robot.Robot() #create an instance of the robot object
r.end_of_arm.get_joint('wrist_yaw').set_velocity(0.1) # rotate CCW at 0.1 rad/s
#for the base of the robot, the set_velocity aapi can take to parameters
r.base.set_velocity(0.01, 0.05) # follow a circular path

r.arm.trajectory.add(t_s=20.0, x_m=0.0, v_m=0.0) # 20 second trajectory extending & retracting the arm