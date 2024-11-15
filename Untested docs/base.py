import stretch_body.robot

r = stretch_body.robot.Robot() #create an instanc of the robot object
r.base.translate_by(0.2) # que a movement by 0.2 meters, but don't execute yet
r.push_command() # execute the preceding commands 
r.base.rotate_by(0.1) # 0.1 radians
r.push_command()