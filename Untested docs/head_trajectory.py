
from __future__ import print_function
import stretch_body.scope
import stretch_body.robot
from stretch_body.hello_utils import *

import sys
import time
import argparse

r=stretch_body.robot.Robot()
r.startup()
# run this command first in the terminal: stretch_trajectory_jog.py --full_body
# the parameters are time, position, velocity
#each trajectory.add command give the robot a point that it must pass through 
# at a given time from running the python file
r.head.get_joint('head_tilt').trajectory.add(t_s=5.0, x_r=(0.0), v_r=0.0)
r.head.get_joint('head_tilt').trajectory.add(t_s=13.0, x_r=(-2.0), v_r=0.0)
r.head.get_joint('head_tilt').trajectory.add(t_s=20.0, x_r=(0.0), v_r=0.0)

r.head.get_joint('head_pan').trajectory.add(t_s=5.0, x_r=(0.0), v_r=0.0)
r.head.get_joint('head_pan').trajectory.add(t_s=12.0, x_r=(-4.0), v_r=0.0)
r.head.get_joint('head_pan').trajectory.add(t_s=20.0, x_r=(0.0), v_r=0.0)
