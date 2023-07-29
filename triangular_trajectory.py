#Triangular Trajectory
import time
from flyt_python import api

# Named Constants
SIDE_LENGTH = 10.0
FLIGHT_HEIGHT = 5.0

# Create an instance of the FlytAPI navigation class to control the drone
flyt_drone = api.navigation(timeout=120000)

# Wait for 3 seconds to allow the drone to initialize
time.sleep(3)

try:
    # Take off the drone to a height of 10 meters
    print(f'1. Taking off till height of {FLIGHT_HEIGHT} meters...')
    flyt_drone.take_off(FLIGHT_HEIGHT)
    print(f'Drone is now at {FLIGHT_HEIGHT} meters height.')

    # Move the drone in a triangular trajectory of side length {SIDE_LENGTH} meters at a height of {FLIGHT_HEIGHT} meters

    # Move from Point A to Point B of triangle ABC (Take a 90-degree turn)
    print('2. Moving from Point A to Point B of triangle ABC (Taking a 90-degree turn)...')
    flyt_drone.position_set(SIDE_LENGTH * 0.8, SIDE_LENGTH * 0.6, FLIGHT_HEIGHT, relative=True)

    # Move from Point B to Point C of triangle ABC (Take a 120-degree turn to form an equilateral triangle)
    print('3. Moving from Point B to Point C of triangle ABC (Taking a 120-degree turn to form an equilateral triangle)...')
    flyt_drone.position_set(-SIDE_LENGTH * 0.4, SIDE_LENGTH * 0.6, 0, relative=True)

    # Move back to the home position from Point C to Point A of triangle ABC (Take a 120-degree turn to complete the triangle)
    print('4. Moving back to the home position from Point C to Point A of triangle ABC (Taking a 120-degree turn to complete the triangle)...')
    flyt_drone.position_set(-SIDE_LENGTH * 0.4, -SIDE_LENGTH * 0.6, 0, relative=True)

    # Land the drone
    print('5. Drone is landing...')
    flyt_drone.land(async=False)

except Exception as e:
    print(f'Error occurred: {e}')

finally:
    # Shutdown the instance
    flyt_drone.disconnect()
