"""Project 2 - Robot Data Manager (STARTER).

Implement each function. Keep the names and signatures - the tests use them.
"""
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "robots.json"
VALID_STATUSES = {"active", "idle", "charging", "error"}


class InvalidRobotDataError(ValueError):
    """Raised when robot data is missing fields or has invalid values."""


def validate_robot(robot: dict) -> dict:
    """Return `robot` if valid, otherwise raise InvalidRobotDataError.

    Required: id (int), name (str), battery (0-100), status (VALID_STATUSES).
    """
    # TODO
    pass


def load_robots(filepath=DATA_FILE) -> list:
    """Load and validate robots from a JSON file.

    - Missing file  -> return []
    - Corrupt JSON  -> raise InvalidRobotDataError
    """
    # TODO: use `with open(...)` and try/except
    pass


def save_robots(robots: list, filepath=DATA_FILE) -> None:
    """Write robots to a JSON file (create parent folders if needed)."""
    # TODO
    pass


def add_robot(robots: list, robot: dict) -> list:
    """Validate and append a robot. Raise InvalidRobotDataError on duplicate id."""
    # TODO
    pass


def find_robot(robots: list, robot_id: int):
    """Return the robot dict with this id, or None."""
    # TODO
    pass


def update_battery(robots: list, robot_id: int, battery: float) -> dict:
    """Update a robot's battery. KeyError if not found; InvalidRobotDataError if out of range."""
    # TODO
    pass


def generate_report(robots: list, filepath) -> Path:
    """Write a human-readable text report and return its Path."""
    # TODO
    pass


def main() -> None:
    """Demo: load, add, update, save, report - with error handling."""
    # TODO
    pass


if __name__ == "__main__":
    main()
