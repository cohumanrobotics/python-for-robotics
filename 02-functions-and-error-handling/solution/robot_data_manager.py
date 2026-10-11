"""Project 2 - Robot Data Manager (SOLUTION)."""
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "robots.json"
REPORT_FILE = Path(__file__).parent / "robot_report.txt"
VALID_STATUSES = {"active", "idle", "charging", "error"}


class InvalidRobotDataError(ValueError):
    """Raised when robot data is missing fields or has invalid values."""


def _is_number(value) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def validate_robot(robot: dict) -> dict:
    """Return `robot` if valid, otherwise raise InvalidRobotDataError."""
    if not isinstance(robot, dict):
        raise InvalidRobotDataError("Robot must be a dictionary")
    for field in ("id", "name", "battery", "status"):
        if field not in robot:
            raise InvalidRobotDataError(f"Missing field: {field}")
    if not isinstance(robot["id"], int) or isinstance(robot["id"], bool):
        raise InvalidRobotDataError("id must be an integer")
    if not isinstance(robot["name"], str) or not robot["name"].strip():
        raise InvalidRobotDataError("name must be a non-empty string")
    if not _is_number(robot["battery"]) or not 0 <= robot["battery"] <= 100:
        raise InvalidRobotDataError("battery must be a number between 0 and 100")
    if robot["status"] not in VALID_STATUSES:
        raise InvalidRobotDataError(f"status must be one of {sorted(VALID_STATUSES)}")
    return robot


def load_robots(filepath=DATA_FILE) -> list:
    """Load and validate robots from a JSON file."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as exc:
        raise InvalidRobotDataError(f"Corrupted data file: {exc}") from exc
    if not isinstance(data, list):
        raise InvalidRobotDataError("Data file must contain a list of robots")
    return [validate_robot(robot) for robot in data]


def save_robots(robots: list, filepath=DATA_FILE) -> None:
    """Write robots to a JSON file."""
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(robots, file, indent=2)


def add_robot(robots: list, robot: dict) -> list:
    """Validate and append a robot; reject duplicate ids."""
    validate_robot(robot)
    if find_robot(robots, robot["id"]) is not None:
        raise InvalidRobotDataError(f"Robot id {robot['id']} already exists")
    robots.append(robot)
    return robots


def find_robot(robots: list, robot_id: int):
    """Return the robot with this id, or None."""
    return next((r for r in robots if r["id"] == robot_id), None)


def update_battery(robots: list, robot_id: int, battery: float) -> dict:
    """Update a robot's battery level."""
    robot = find_robot(robots, robot_id)
    if robot is None:
        raise KeyError(f"Robot {robot_id} not found")
    if not _is_number(battery) or not 0 <= battery <= 100:
        raise InvalidRobotDataError("battery must be a number between 0 and 100")
    robot["battery"] = battery
    return robot


def generate_report(robots: list, filepath=REPORT_FILE) -> Path:
    """Write a text report and return its path."""
    filepath = Path(filepath)
    lines = ["ROBOT FLEET REPORT", "=" * 40]
    for robot in robots:
        lines.append(
            f"#{robot['id']:<3} {robot['name']:<10} "
            f"battery={robot['battery']:>5.1f}%  status={robot['status']}"
        )
    lines.append("=" * 40)
    lines.append(f"Total robots: {len(robots)}")
    with open(filepath, "w", encoding="utf-8") as file:
        file.write("\n".join(lines) + "\n")
    return filepath


def main() -> None:
    """Demo of the full workflow with error handling."""
    try:
        robots = load_robots()
        print(f"Loaded {len(robots)} robots")

        if find_robot(robots, 4) is None:  # keep the demo re-runnable
            add_robot(robots, {"id": 4, "name": "Drone-X", "battery": 95, "status": "active"})
        update_battery(robots, 2, 75)

        try:
            add_robot(robots, {"id": 4, "name": "Duplicate", "battery": 50, "status": "idle"})
        except InvalidRobotDataError as exc:
            print(f"Expected error handled: {exc}")

        try:
            update_battery(robots, 99, 50)
        except KeyError as exc:
            print(f"Expected error handled: {exc}")

        save_robots(robots)
        report = generate_report(robots)
        print(f"Saved data and wrote report to {report}")
    except InvalidRobotDataError as exc:
        print(f"Data error: {exc}")
    except OSError as exc:
        print(f"File error: {exc}")


if __name__ == "__main__":
    main()
