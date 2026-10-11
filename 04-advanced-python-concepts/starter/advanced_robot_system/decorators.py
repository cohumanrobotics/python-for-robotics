"""Decorators (STARTER)."""
import functools
import logging
import time

logger = logging.getLogger("robot")


def timer(func):
    """Print how long `func` takes to run."""
    # TODO: use functools.wraps and time.perf_counter
    return func


def log_calls(func):
    """Log the function name, arguments and result."""
    # TODO
    return func


def validate_speed(max_speed):
    """Decorator factory: first argument is a speed that must be 0..max_speed."""
    def decorator(func):
        # TODO: raise ValueError for invalid speed
        return func
    return decorator
