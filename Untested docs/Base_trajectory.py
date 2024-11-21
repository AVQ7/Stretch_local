
import stretch_body.robot
import time
r=stretch_body.robot.Robot()
r.startup()

# run this command first in the terminal: stretch_trajectory_jog.py --full_body

r.base.trajectory.add(time=0.0, x=0,y=0, theta=deg_to_rad(0.0), translational_vel=0.0, rotational_vel=0.0 )
r.base.trajectory.add(time=10.0, x=0,y=0, theta=deg_to_rad(180.0), translational_vel=0.0, rotational_vel=0.0)
r.base.trajectory.add(time=20.0,  x=0,y=0,theta=deg_to_rad(0.0), translational_vel=0.0, rotational_vel=0.0)
