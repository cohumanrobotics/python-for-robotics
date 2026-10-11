"""Project 1 - Complete Robot Control System (STARTER).

Complete every TODO. Run the file and test with different inputs.
"""

# ---------------------------------------------------------------------------
# 1. CONSTANTS
# ---------------------------------------------------------------------------
# TODO: define MAX_SPEED (float), MIN_BATTERY (int, %), MAX_TEMPERATURE (float, C)


# ---------------------------------------------------------------------------
# 2. ROBOT CONFIGURATION (input)
# ---------------------------------------------------------------------------
print("=== Robot Configuration ===")
# TODO: ask for robot name (str), robot ID (int), current speed (float),
#       battery (int), temperature (float), number of waypoints (int)


# TODO: build a `waypoints` list of (x, y) tuples with a for loop
waypoints = []
position = (0.0, 0.0)  # robot starts at the origin


# ---------------------------------------------------------------------------
# 3. SAFETY CHECKS (comparison + logical operators + if/else)
# ---------------------------------------------------------------------------
emergency = False
# TODO: battery below MIN_BATTERY      -> warning + emergency = True
# TODO: temperature above MAX_TEMPERATURE -> warning + emergency = True
# TODO: speed above MAX_SPEED          -> warning
# TODO: low battery AND high temperature -> print "CRITICAL" message


# ---------------------------------------------------------------------------
# 4. WAYPOINT PROCESSING (for loop + arithmetic)
# ---------------------------------------------------------------------------
total_distance = 0.0
# TODO: loop over waypoints; distance = ((dx ** 2) + (dy ** 2)) ** 0.5
#       add to total_distance and update `position`


# ---------------------------------------------------------------------------
# 5. STATUS REPORT (formatted output)
# ---------------------------------------------------------------------------
print("\n=== STATUS REPORT ===")
# TODO: print name, ID, speed, battery, temperature, position,
#       waypoint count, total distance, and the final status
#       ("EMERGENCY" if emergency else "All systems nominal")
