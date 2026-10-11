"""Context managers (STARTER)."""
from contextlib import contextmanager


@contextmanager
def robot_operation(name):
    """Print start / complete / cleanup messages around a robot operation."""
    # TODO: use try / except / else / finally around `yield`
    yield


class RobotSession:
    """Class-based context manager that records the duration and any error."""

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        # TODO
        return self

    def __exit__(self, exc_type, exc, tb):
        # TODO: always clean up; return False so exceptions propagate
        return False
