"""Demo script for the Robot Management System (SOLUTION)."""
from robot_system import Robot, GroundRobot, AerialRobot, WarehouseRobot


def main():
    robot1 = GroundRobot("Rover", battery=80)
    robot2 = AerialRobot("Skyhawk", battery=60)
    robot3 = WarehouseRobot("Hauler", max_weight=40, battery=90)
    robot3.load_package(25)

    robots = [robot1, robot2, robot3]

    print("--- Polymorphism ---")
    for robot in robots:
        print(robot.move(10))

    print("\n--- Status ---")
    for robot in robots:
        print(robot.get_status())

    print("\n--- Sorted by battery ---")
    for robot in sorted(robots):
        print(str(robot))

    print("\n--- repr ---")
    print(repr(robot1))

    print("\n--- Class & static methods ---")
    print("Total robots:", Robot.get_total_robots())
    print("Distance (0,0)->(3,4):", Robot.calculate_distance(0, 0, 3, 4))


if __name__ == "__main__":
    main()
