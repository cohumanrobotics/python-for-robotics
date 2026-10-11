"""Project 1 - Complete Robot Control System (SOLUTION)."""

# 1. CONSTANTS
MAX_SPEED = 100.0        # km/h
MIN_BATTERY = 20         # percent
MAX_TEMPERATURE = 50.0   # degrees Celsius

# 2. ROBOT CONFIGURATION
print("=== Robot Configuration ===")
robot_name = input("Robot name: ")
robot_id = int(input("Robot ID: "))
current_speed = float(input("Current speed (km/h): "))
battery = int(input("Battery level (%): "))
temperature = float(input("Temperature (C): "))
num_waypoints = int(input("Number of waypoints: "))

waypoints = []
for i in range(num_waypoints):
    x = float(input(f"  Waypoint {i + 1} - x: "))
    y = float(input(f"  Waypoint {i + 1} - y: "))
    waypoints.append((x, y))

position = (0.0, 0.0)
is_operational = True

# 3. SAFETY CHECKS
print("\n=== Safety Checks ===")
emergency = False

if battery < MIN_BATTERY:
    print(f"WARNING: Low battery ({battery}% < {MIN_BATTERY}%)")
    emergency = True
else:
    print("Battery OK")

if temperature > MAX_TEMPERATURE:
    print(f"WARNING: High temperature ({temperature}C > {MAX_TEMPERATURE}C)")
    emergency = True
else:
    print("Temperature OK")

if current_speed > MAX_SPEED:
    print(f"WARNING: Speed {current_speed} exceeds maximum {MAX_SPEED}")
    current_speed = MAX_SPEED
    print(f"Speed limited to {current_speed}")
else:
    print("Speed OK")

if battery < MIN_BATTERY and temperature > MAX_TEMPERATURE:
    print("CRITICAL: Low battery AND high temperature - shut down immediately!")
    is_operational = False

# 4. WAYPOINT PROCESSING
print("\n=== Waypoint Processing ===")
total_distance = 0.0
for index, (wx, wy) in enumerate(waypoints, start=1):
    dx = wx - position[0]
    dy = wy - position[1]
    distance = ((dx ** 2) + (dy ** 2)) ** 0.5
    total_distance += distance
    position = (wx, wy)
    print(f"Waypoint {index}: ({wx}, {wy}) - distance {distance:.2f}")

if current_speed > 0:
    eta_hours = total_distance / current_speed
    print(f"Estimated travel time: {eta_hours:.2f} h")

# 5. STATUS REPORT
print("\n=== STATUS REPORT ===")
print(f"Robot:          {robot_name} (ID {robot_id})")
print(f"Speed:          {current_speed:.1f} km/h (max {MAX_SPEED})")
print(f"Battery:        {battery}%")
print(f"Temperature:    {temperature:.1f}C")
print(f"Position:       {position}")
print(f"Waypoints:      {len(waypoints)}")
print(f"Total distance: {total_distance:.2f}")
print(f"Operational:    {is_operational}")
print(f"Status:         {'EMERGENCY' if emergency else 'All systems nominal'}")
