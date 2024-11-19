import stretch_body.robot
r = stretch_body.robot.Robot() #always create robot object
did_startup = r.startup()
print(f'Robot connected to hardware: {did_startup}')


is_homed = r.is_homed()
print(f'Robot is homed: {is_homed}')

r.base.translate_by(-0.9) # que a movement by 0.9 meters forward, but don't execute yet, negative numbers mean forward
r.push_command() # execute the preceding commands 
r.base.rotate_by(-6.28) # 6.28 radians clockwise. positive input would be counterclockwise
r.push_command()