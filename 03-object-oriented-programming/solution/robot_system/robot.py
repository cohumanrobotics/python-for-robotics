"""Robot class hierarchy (SOLUTION)."""
import math


class Robot:
    """Base class for all robots."""

    total_robots = 0

    def __init__(self, name, battery=100, position=(0.0, 0.0)):
        self._name = name
        self._battery = 100
        self.battery = battery  # goes through the validating setter
        self._position = tuple(position)
        Robot.total_robots += 1

    # ----- properties -----
    @property
    def name(self):
        return self._name

    @property
    def battery(self):
        return self._battery

    @battery.setter
    def battery(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Battery must be between 0 and 100")
        self._battery = value

    @property
    def position(self):
        return self._position

    # ----- behaviour -----
    def move(self, distance):
        raise NotImplementedError("Subclasses must implement move()")

    def get_status(self):
        x, y = self._position
        return f"{self._name}: battery={self._battery:.1f}%, position=({x:.1f}, {y:.1f})"

    def _drain(self, cost):
        """Consume battery; return False (and don't move) if not enough."""
        if cost > self._battery:
            return False
        self.battery = self._battery - cost
        return True

    # ----- special methods -----
    def __str__(self):
        return f"{type(self).__name__} '{self._name}' ({self._battery:.0f}% battery)"

    def __repr__(self):
        return (f"{type(self).__name__}(name={self._name!r}, "
                f"battery={self._battery!r}, position={self._position!r})")

    def __eq__(self, other):
        if not isinstance(other, Robot):
            return NotImplemented
        return self._name == other._name

    def __lt__(self, other):
        if not isinstance(other, Robot):
            return NotImplemented
        return self._battery < other._battery

    def __hash__(self):
        return hash(self._name)

    # ----- class & static methods -----
    @classmethod
    def get_total_robots(cls):
        return Robot.total_robots

    @staticmethod
    def calculate_distance(x1, y1, x2, y2):
        return math.hypot(x2 - x1, y2 - y1)


class GroundRobot(Robot):
    """Drives along the x-axis; 0.5% battery per unit."""

    BATTERY_PER_UNIT = 0.5

    def move(self, distance):
        if not self._drain(distance * self.BATTERY_PER_UNIT):
            return f"{self.name} has too little battery to drive {distance}"
        x, y = self._position
        self._position = (x + distance, y)
        return f"{self.name} drove {distance} units on the ground"


class AerialRobot(Robot):
    """Flies along the y-axis; 1% battery per unit."""

    BATTERY_PER_UNIT = 1.0

    def move(self, distance):
        if not self._drain(distance * self.BATTERY_PER_UNIT):
            return f"{self.name} has too little battery to fly {distance}"
        x, y = self._position
        self._position = (x, y + distance)
        return f"{self.name} flew {distance} units through the air"


class WarehouseRobot(GroundRobot):
    """Ground robot that carries packages."""

    def __init__(self, name, max_weight=50, battery=100, position=(0.0, 0.0)):
        super().__init__(name, battery, position)
        self._max_weight = max_weight
        self._current_weight = 0

    @property
    def max_weight(self):
        return self._max_weight

    @property
    def current_weight(self):
        return self._current_weight

    def load_package(self, weight):
        if weight <= 0:
            raise ValueError("Weight must be positive")
        if self._current_weight + weight > self._max_weight:
            return False
        self._current_weight += weight
        return True

    def unload_package(self):
        released, self._current_weight = self._current_weight, 0
        return released

    def move(self, distance):
        # heavier loads drain extra battery
        load_factor = 1 + self._current_weight / self._max_weight
        if not self._drain(distance * self.BATTERY_PER_UNIT * load_factor):
            return f"{self.name} has too little battery to carry the load"
        x, y = self._position
        self._position = (x + distance, y)
        return f"{self.name} delivered {self._current_weight}kg over {distance} units"
