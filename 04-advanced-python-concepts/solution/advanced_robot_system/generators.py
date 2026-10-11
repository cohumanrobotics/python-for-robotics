"""Generators for streaming robot data."""
import math
import random
from collections import namedtuple

Waypoint = namedtuple("Waypoint", ["x", "y"])
WaypointInfo = namedtuple("WaypointInfo", ["index", "position", "distance"])


def process_waypoints(waypoints, start=(0.0, 0.0)):
    """Yield WaypointInfo(index, position, distance_from_previous) lazily."""
    previous = tuple(start)
    for index, point in enumerate(waypoints):
        position = tuple(point)
        yield WaypointInfo(index, position, round(math.dist(previous, position), 2))
        previous = position


def sensor_stream(count, seed=None):
    """Yield `count` simulated sensor readings one at a time."""
    rng = random.Random(seed)
    for _ in range(count):
        yield round(rng.uniform(0.0, 100.0), 2)
