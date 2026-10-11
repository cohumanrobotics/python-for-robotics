"""Reusable decorators."""
import functools
import logging
import time

logger = logging.getLogger("robot")


def timer(func):
    """Print how long `func` takes to run."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - start
            print(f"[timer] {func.__name__} took {elapsed:.6f}s")
    return wrapper


def log_calls(func):
    """Log the function name, arguments and result."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info("Calling %s", func.__name__)
        result = func(*args, **kwargs)
        logger.info("%s returned %r", func.__name__, result)
        return result
    return wrapper


def validate_speed(max_speed):
    """Decorator factory: first positional argument must be 0..max_speed."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(speed, *args, **kwargs):
            if not 0 <= speed <= max_speed:
                raise ValueError(f"Speed {speed} outside 0..{max_speed}")
            return func(speed, *args, **kwargs)
        return wrapper
    return decorator
