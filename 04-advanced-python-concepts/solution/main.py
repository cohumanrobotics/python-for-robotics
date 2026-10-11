"""Demo script for the Advanced Robot System (SOLUTION)."""
import logging
import sys

from advanced_robot_system.analysis import (
    analyze_fleet, battery_pipeline, group_by_type, good_battery)
from advanced_robot_system.context_managers import RobotSession, robot_operation
from advanced_robot_system.generators import process_waypoints, sensor_stream

ROBOTS = [
    {"name": "Atlas", "type": "ground", "battery": 85, "status": "active"},
    {"name": "Scout", "type": "aerial", "battery": 40, "status": "idle"},
    {"name": "Hauler", "type": "ground", "battery": 12, "status": "charging"},
    {"name": "Falcon", "type": "aerial", "battery": 92, "status": "active"},
]

WAYPOINTS = [(0, 3), (4, 3), (4, 0), (10, 8)]


def main():
    logging.basicConfig(level=logging.INFO, format="[log] %(message)s")

    print("--- Fleet analysis (decorated) ---")
    print(analyze_fleet(ROBOTS))

    print("\n--- Grouping & pipeline ---")
    print(dict(group_by_type(ROBOTS)))
    print(battery_pipeline(ROBOTS))
    print([r["name"] for r in good_battery(ROBOTS, 80)])

    print("\n--- Waypoint generator inside a context manager ---")
    with robot_operation("Patrol"):
        for info in process_waypoints(WAYPOINTS):
            print(info)

    with RobotSession("Telemetry") as session:
        readings = list(sensor_stream(5, seed=1))
        print("Readings:", readings)
    print(f"Session took {session.duration:.6f}s")

    print("\n--- Memory: list vs generator ---")
    as_list = [n * n for n in range(100_000)]
    as_gen = (n * n for n in range(100_000))
    print(f"list:      {sys.getsizeof(as_list):>10,} bytes")
    print(f"generator: {sys.getsizeof(as_gen):>10,} bytes")


if __name__ == "__main__":
    main()
