#!/usr/bin/env python
import time
from flyt_python import api

drone = api.navigation(timeout=120000)  # instance of flyt droneigation class

time.sleep(3)

print '1. taking off till height of 5m'
drone.take_off(5.0)
print 'Current position is at 5m height at point A'

print ' move in a square trajectory of side length 6.5m at a height of 5m'

print ' 2. moving to Point B from intial Point A'
drone.position_set(0, 6.5, 0, yaw=1.0472, relative=True)

print ' 3. moving to Point C from Point B'
drone.position_set(6.5, 0, 0, relative=True)

print ' 4. moving to Point D from Point C'
drone.position_set(0, -6.5, 0, relative=True)

print ' 5. moving back to the initial Point A from Point D'
drone.position_set(-6.5, 0, 0, relative=True)

print '     6. Landing'
drone.land(async=False)

# shutdown the instance
drone.disconnect()
