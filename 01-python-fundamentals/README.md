# Project 1: Complete Robot Control System

## Learning Goals
- Combine all concepts into a complete program
- Practice problem-solving
- Build a functional robot control system
- Verify your understanding

## Requirements
1. **Variables and Constants** – robot name, ID, `MAX_SPEED`, `MIN_BATTERY`, `MAX_TEMPERATURE`; current speed, battery, position
2. **Data Types** – strings, integers, floats, booleans, lists
3. **Input/Output** – get configuration with `input()`, show a formatted status report
4. **Operators** – arithmetic (`+ - * **`) for distances/speeds, comparison (`< > <=`) for safety checks
5. **Flow Control** – `if/else`, `for` loop over waypoints, logical `and` for combined conditions

## Practice Scenarios
- Low battery (< 20%)
- High temperature (> 50 °C)
- Speed above maximum
- Multiple waypoints

## Verification
Your program should accept all inputs, run all safety checks, process waypoints
(calculating distances) and display a complete status report.

## Run
```bash
cd starter
python robot_control_system.py
```

## Folder Guide

- `starter/` – start here; complete the `TODO`s
- `solution/` – reference solution; compare only after you've tried it yourself
