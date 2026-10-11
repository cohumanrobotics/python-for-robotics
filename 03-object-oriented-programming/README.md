# Project 3: Robot Management System

## Learning Goals
- Combine all Object-Oriented Programming concepts
- Build a complete robot system
- Practice real-world OOP design

## Requirements
1. **Core `Robot` class** – `__init__`, attributes `name`, `battery`, `position`; methods `move()` (overridden by subclasses) and `get_status()`. Create at least two robots.
2. **Special methods** – `__str__`, `__repr__`, `__eq__`, `__lt__` (sorting by battery).
3. **Inheritance** – e.g. `WarehouseRobot` with `max_weight`, `current_weight`, overridden `move()`, `load_package()`, `unload_package()`.
4. **Class & static methods** – class attribute `total_robots`, `@classmethod` returning the count, `@staticmethod` `calculate_distance(x1, y1, x2, y2)`.
5. **Encapsulation** – protected/private attributes, `@property` getters, validating setters (battery 0-100).
6. **Polymorphism** – `GroundRobot`, `AerialRobot`; loop over a list and call `robot.move(10)`.

## Success Criteria
Create and use classes, apply inheritance, use encapsulation with properties,
implement polymorphism; explain class vs instance attributes and when to use
inheritance.

## Run
```bash
cd starter      # or solution
python main.py
```

## Folder Guide

- `starter/` – start here; complete the `TODO`s
- `solution/` – reference solution; compare only after you've tried it yourself
