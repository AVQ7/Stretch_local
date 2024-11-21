import stretch_body.robot
import time
r=stretch_body.robot.Robot()
r.startup()
# run this command first in the terminal: stretch_trajectory_jog.py --full_body

#Define the waypoints, make the rist roll, one way, and back to its original position.
r.end_of_arm.motors['wrist_roll'].trajectory.add(t_s=0.0, x_r=0, v_r=0.0)
r.end_of_arm.motors['wrist_roll'].trajectory.add(t_s=5.0, x_r=-3.5, v_r= 0.0)
r.end_of_arm.motors['wrist_roll'].trajectory.add(t_s=10.0, x_r=0.0,v_r=0.0)

#Begin execution
r.end_of_arm.follow_trajectory()

#Wait unti completion
while r.end_of_arm.is_trajectory_active():
    print('Execution time: %f'%r.end_of_arm.get_joint('wrist_roll').get_trajectory_time_remaining())
    time.sleep(0.1)

r.stop()