import stretch_body.robot

r = stretch_body.robot.Robot() #always create robot object
r = stretch_body.robot.Robot() #always create robot object
did_startup = r.startup()
print(f'Robot connected to hardware: {did_startup}')


is_homed = r.is_homed()
print(f'Robot is homed: {is_homed}')
r.lift.move_to(-0.3) # moves the lift up, down or not at all 
r.push_command()
#deppending on whether its at position 0.2 meeters.
r.lift.move_by(-0.3) # moves lift +0.1 meters relative to current position
r.push_command() # execute previous commands ina sequence
r.time.sleep(2.0) #This line pauses the execution of successsive the code 
# for given time
r.arm.wait_until_at_setpoint() # alternatively, we could polling method instead to wait
#untill previous motion completes
r.stop() # safety measure that halts any robot movementimmediatly 

