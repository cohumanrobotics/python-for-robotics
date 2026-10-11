"""Generators (STARTER)."""
from collections import namedtuple

Waypoint = namedtuple("Waypoint", ["x", "y"])
WaypointInfo = namedtuple("WaypointInfo", ["index", "position", "distance"])


def process_waypoints(waypoints, start=(0.0, 0.0)):
    """Yield WaypointInfo(index, position, distance_from_previous) lazily."""
    # TODO
    yield from ()


def sensor_stream(count, seed=None):
    """Yield `count` simulated sensor readings (floats) one at a time."""
    # TODO
    yield from ()
