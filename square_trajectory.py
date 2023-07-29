# Square Trajectory
import time
from flyt_python import api

# Constants
SIDE_LENGTH = 6.5
FLIGHT_HEIGHT = 5.0
TURN_ANGLE = 90.0

# Function to move the drone to a specified position
def move_to(drone, x, y, z, relative=True):
    drone.position_set(x, y, z, relative=relative)

# Function to perform the square trajectory
def square_trajectory(drone):
    print('1. Drone is taking off to a height of 5 meters...')
    drone.take_off(FLIGHT_HEIGHT)
    print('Drone is now at 5 meters height.')

    print(f'2. Moving drone to Point B of the square ABCD (Taking a {TURN_ANGLE}-degree turn)...')
    move_to(drone, SIDE_LENGTH, 0, 0, relative=True)

    print(f'3. Moving drone to Point C of the square ABCD (Taking a {TURN_ANGLE}-degree turn)...')
    move_to(drone, 0, SIDE_LENGTH, 0, relative=True)

    print(f'4. Moving drone back to Point D of square ABCD (Taking a {TURN_ANGLE}-degree turn)...')
    move_to(drone, -SIDE_LENGTH, 0, 0, relative=True)

    print(f'5. Moving drone back to Point A of square ABCD to complete the square trajectory (Taking a {TURN_ANGLE}-degree turn)...')
    move_to(drone, 0, -SIDE_LENGTH, 0, relative=True)

# Main function to control the drone
def main():
    # Create an instance of the FlytAPI navigation class to control the drone
    drone = api.navigation(timeout=120000)

    # Wait for 3 seconds to allow the drone to initialize
    time.sleep(3)

    try:
        # Perform the square trajectory
        square_trajectory(drone)

        # Land the drone
        print('6. Drone is landing...')
        drone.land(async=False)

    except Exception as e:
        print(f'Error occurred: {e}')

    finally:
        # Disconnect the drone instance
        drone.disconnect()

if __name__ == "__main__":
    main()
