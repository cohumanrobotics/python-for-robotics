"""Data processing helpers (STARTER)."""
from collections import Counter, defaultdict

from .decorators import log_calls, timer


def filter_active(robots):
    """List comprehension: robots whose status is 'active'."""
    # TODO
    return []


def good_battery(robots, minimum=50):
    """Generator expression: robots with battery >= minimum."""
    # TODO
    return iter(())


def count_statuses(robots):
    """Counter of robot statuses."""
    # TODO
    return Counter()


def group_by_type(robots):
    """defaultdict(list) mapping robot type -> list of robot names."""
    # TODO
    return defaultdict(list)


def battery_pipeline(robots, minimum=30):
    """filter -> map -> sorted, using lambda. Return names sorted by battery desc."""
    # TODO
    return []


@timer
@log_calls
def analyze_fleet(robots):
    """Return a summary dict: total, active, avg_battery, status_counts."""
    # TODO
    return {}
