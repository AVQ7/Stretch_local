
import stretch_body.robot
import time
r=stretch_body.robot.Robot()
r.startup()

# run this command first in the terminal: stretch_trajectory_jog.py --full_body
#Define the waypoints
r.lift.trajectory.add(t_s=0.0, x_m=0.2, v_m=0.0)
r.lift.trajectory.add(t_s=10.0, x_m=0.9, v_m=0.0)
r.lift.trajectory.add(t_s=20.0, x_m=0.2, v_m=0.0)

#Begin execution
r.lift.follow_trajectory()

#Wait unti completion
while r.lift.is_trajectory_active():
    print('Execution time: %f'%r.lift.get_trajectory_time_remaining())
    time.sleep(0.1)

r.stop()