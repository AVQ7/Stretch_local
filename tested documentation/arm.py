import stretch_body.robot

r = stretch_body.robot.Robot() #always create robot object
r = stretch_body.robot.Robot() #always create robot object
did_startup = r.startup()
print(f'Robot connected to hardware: {did_startup}')


is_homed = r.is_homed()
print(f'Robot is homed: {is_homed}')
r.arm.move_by(0.1) # moves the arm moves to position 0.2 meters, not rlative
#r.arm.move_by(0.1) # moves arm +0.1 meters relative to current position
r.push_command()
#r.time.sleep(2.0) #This line pauses the execution of the code for 2 seconds

##r.stop() # safety measure that halts any robot movementimmediatly 

