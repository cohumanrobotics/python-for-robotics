"""Robot class hierarchy (STARTER). Complete every TODO."""
import math


class Robot:
    """Base class for all robots."""

    total_robots = 0  # class attribute shared by all robots

    def __init__(self, name, battery=100, position=(0.0, 0.0)):
        # TODO: store _name, _battery (use the validating setter), _position
        # TODO: increment Robot.total_robots
        pass

    # --- properties (encapsulation) ---
    # TODO: @property name
    # TODO: @property battery  +  @battery.setter (raise ValueError outside 0-100)
    # TODO: @property position

    # --- behaviour ---
    def move(self, distance):
        """Subclasses override this."""
        raise NotImplementedError

    def get_status(self):
        # TODO: return a string with name, battery and position
        pass

    # --- special methods ---
    # TODO: __str__ (friendly), __repr__ (developer), __eq__ (same name),
    #       __lt__ (compare battery), __hash__

    # --- class & static methods ---
    # TODO: @classmethod get_total_robots(cls)
    # TODO: @staticmethod calculate_distance(x1, y1, x2, y2)


class GroundRobot(Robot):
    """Moves along the x-axis. Uses 0.5% battery per unit."""

    def move(self, distance):
        # TODO
        pass


class AerialRobot(Robot):
    """Moves along the y-axis (flying). Uses 1% battery per unit."""

    def move(self, distance):
        # TODO
        pass


class WarehouseRobot(GroundRobot):
    """Ground robot that carries packages."""

    def __init__(self, name, max_weight=50, battery=100, position=(0.0, 0.0)):
        # TODO: call super().__init__ and set max_weight / current_weight
        pass

    def load_package(self, weight):
        # TODO: reject if over max_weight
        pass

    def unload_package(self):
        # TODO
        pass

    def move(self, distance):
        # TODO: heavier loads drain more battery
        pass
