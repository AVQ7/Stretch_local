
import stretch_body.robot
r=stretch_body.robot.Robot()
r.startup()
#trajectory as splines documentation:
#https://docs.hello-robot.com/0.2/stretch-tutorials/stretch_body/tutorial_splined_trajectories/
#you could check this repo with examples:
# https://github.com/hello-robot/stretch_body/blob/master/tools/bin/stretch_trajectory_jog.py
# drawing a smooth circle using the lyft/arm trajectory: 
# https://forum.hello-robot.com/t/creating-smooth-motion-using-trajectories/671

# run this command first in the terminal: stretch_trajectory_jog.py --full_body
#Define the waypoints
times = [0.0, 10.0, 20.0]
positions = [r.arm.status['pos'], 0.45, 0.0]
velocities = [r.arm.status['vel'], 0.0, 0.0]

#Create the spline trajectory
for waypoint in zip(times, positions, velocities):
    r.arm.trajectory.add(waypoint[0], waypoint[1], waypoint[2])

#Begin execution
r.arm.follow_trajectory()

#Wait unti completion
while r.arm.is_trajectory_active():
    print('Execution time: %f'%r.arm.get_trajectory_time_remaining())
    time.sleep(0.1)

r.stop()