import stretch_body.robot

r = stretch_body.robot.Robot() #always create robot object
r.lift.move_to(0.2) # moves the lift up, down or not at all 
#deppending on whether its at position 0.2 meeters.
r.lift.move_by(0.1) # moves lift +0.1 meters relative to current position
r.push_command() # execute previous commands ina sequence
r.time.sleep(2.0) #This line pauses the execution of successsive the code 
# for given time
r.arm.wait_until_at_setpoint() # alternatively, we could polling method instead to wait
#untill previous motion completes
r.stop() # safety measure that halts any robot movementimmediatly 

