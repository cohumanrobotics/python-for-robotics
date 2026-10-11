# Project 4: Advanced Robot Software System

## Your Project
Create a robot processing system using advanced Python features:
comprehensions, generators, decorators and context managers.

## Requirements
1. **Decorators** – measure execution time, log calls (and validate speed); apply to a main function.
2. **Context managers** – `@contextmanager` for a robot start/complete lifecycle, plus a class-based version.
3. **Generators** – process waypoints, yielding `(index, position, distance)`.
4. **Comprehensions** – list comprehensions to filter active robots; generator expressions for efficient iteration.
5. **Advanced collections** – `Counter` (statuses), `defaultdict` (group by type), `namedtuple` (waypoints).
6. **Functional processing** – `lambda`, `map()`, `filter()`, `sorted(key=...)` pipelines.

## Challenges
- Comprehension-powered data filters (sensor conversion, distant waypoints, good battery)
- Streaming generators (show memory efficiency vs lists)
- Decorated robot APIs (logging, validation, timing)
- Robust context managers (function- and class-based, guaranteed cleanup)
- Functional pipelines (navigation data, telemetry summary)

## Success Criteria
Use comprehensions & generators, create decorators, use context managers, apply
advanced data structures, and organise code into modules/packages.

## Run
```bash
cd starter      # or solution
python main.py
```

## Folder Guide

- `starter/` – start here; complete the `TODO`s
- `solution/` – reference solution; compare only after you've tried it yourself
