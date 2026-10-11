"""Function-based and class-based context managers."""
import time
from contextlib import contextmanager


@contextmanager
def robot_operation(name):
    """Start / complete / cleanup lifecycle for a robot operation."""
    print(f"[start] {name}")
    try:
        yield
    except Exception as exc:
        print(f"[failed] {name}: {exc}")
        raise
    else:
        print(f"[complete] {name}")
    finally:
        print(f"[cleanup] {name}")


class RobotSession:
    """Class-based context manager that records duration and any error."""

    def __init__(self, name):
        self.name = name
        self.duration = None
        self.error = None
        self._start = None

    def __enter__(self):
        self._start = time.perf_counter()
        print(f"[session open] {self.name}")
        return self

    def __exit__(self, exc_type, exc, tb):
        self.duration = time.perf_counter() - self._start
        self.error = exc
        print(f"[session closed] {self.name} ({self.duration:.6f}s)")
        return False  # never swallow exceptions
