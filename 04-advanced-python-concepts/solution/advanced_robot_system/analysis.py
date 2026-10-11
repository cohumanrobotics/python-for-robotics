"""Data processing with comprehensions, collections and functional tools."""
from collections import Counter, defaultdict

from .decorators import log_calls, timer


def filter_active(robots):
    return [r for r in robots if r["status"] == "active"]


def good_battery(robots, minimum=50):
    return (r for r in robots if r["battery"] >= minimum)


def count_statuses(robots):
    return Counter(r["status"] for r in robots)


def group_by_type(robots):
    groups = defaultdict(list)
    for robot in robots:
        groups[robot["type"]].append(robot["name"])
    return groups


def battery_pipeline(robots, minimum=30):
    """filter -> sorted -> map: names of robots above `minimum`, best battery first."""
    healthy = filter(lambda r: r["battery"] >= minimum, robots)
    ranked = sorted(healthy, key=lambda r: r["battery"], reverse=True)
    return list(map(lambda r: r["name"], ranked))


@timer
@log_calls
def analyze_fleet(robots):
    total = len(robots)
    avg_battery = sum(r["battery"] for r in robots) / total if total else 0.0
    return {
        "total": total,
        "active": len(filter_active(robots)),
        "avg_battery": round(avg_battery, 1),
        "status_counts": dict(count_statuses(robots)),
    }
