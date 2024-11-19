import stretch_body.robot

r = stretch_body.robot.Robot() #always create robot object
did_startup = r.startup()
print(f'Robot connected to hardware: {did_startup}')


is_homed = r.is_homed()
print(f'Robot is homed: {is_homed}')

r.arm.move_to(0.2) # 0.2 meters
r.push_command()
r.lift.move_to(0.6) # 0.6 meters
r.push_command()