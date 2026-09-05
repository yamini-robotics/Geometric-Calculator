# Geometric Calculator

A simple 2D geometric calculator implemented in Python for the Niqo Robotics Robotics Engineer Evaluation Assignment.

The calculator provides an interactive command-line interface (CLI) similar to Python's REPL. Users can create geometric objects, keep them available during the current session, and perform calculations such as distance between shapes.

## 1. Features

### Required Shapes

The calculator currently supports:

* Point

* Line

* Circle

* Rectangle

### Required Calculations

The calculator supports:

* Point-to-point distance

* Distance between two shapes

* Circle area

* Circle circumference

* Rectangle area

* Rectangle perimeter

* Line length

### Distance Between Shapes

Distance calculations are designed around the minimum Euclidean distance between two shapes.

The supported shape combinations are:

1. Point - Point

2. Point - Line

3. Point - Circle

4. Point - Rectangle

5. Line - Line

6. Line - Circle

7. Line - Rectangle

8. Circle - Circle

9. Circle - Rectangle

10. Rectangle - Rectangle

Both orders are supported where applicable.

For example:

```text

distance(p1, c1)

```

and

```text

distance(c1, p1)

```

represent the same geometric distance.

If two shapes touch or overlap, their distance is considered to be `0`.

---

# 2. Project Structure

The project is divided into separate Python files according to the geometric objects and calculations.

```text

geometric-calculator/

│

├── main.py

├── point.py

├── line.py

├── circle.py

├── rectangle.py

├── distance_between_shapes.py

├── shape3d.py

└── README.md

```

### `point.py`

Contains the `Point` class.

A point is represented by:

```text

Point(x, y)

```

It also provides point-to-point distance calculation.

### `line.py`

Contains the `Line` class.

A line segment is represented using two points:

```text

Line(p1, p2)

```

It provides the length of the line segment.

### `circle.py`

Contains the `Circle` class.

A circle is represented by:

```text

Circle(center, radius)

```

It provides:

* Area

* Circumference

### `rectangle.py`

Contains the `Rectangle` class.

The current implementation represents a rectangle using two opposite corner points:

```text

Rectangle(p1, p2)

```

The rectangle is assumed to be axis-aligned.

It provides:

* Area

* Perimeter

### `distance_between_shapes.py`

Contains the distance calculations between the supported combinations of geometric shapes.

A common public function is:

```text

distance(shape1, shape2)

```

The function identifies the types of the two objects and calls the appropriate distance calculation.

### `main.py`

Contains the interactive REPL-style command-line interface.

It:

* accepts commands from the user

* creates geometric objects

* stores created objects during the current session

* performs calculations

* handles invalid commands without immediately terminating the calculator

---

# 3. Requirements

The project requires:

* Python 3

* A terminal / command prompt

* No external Python libraries are required for the core calculator functionality

---

# 4. Setup

## Step 1: Install Python

Install Python 3 if it is not already installed.

Verify the installation:

```bash

python --version

```

or, depending on the system:

```bash

python3 --version

```

## Step 2: Clone or download the repository

Clone the repository:

```bash

git clone 'https://github.com/yamini-robotics/Geometric-Calculator.git'

```

Move into the project directory:

```bash

cd geometric-calculator

```

## Step 3: No package installation required

The project currently uses only Python's built-in functionality and the project's own modules.

Therefore, there is no `pip install` step for the core calculator.

---

# 5. Running the Calculator

Run:

```bash

python main.py

```

The calculator will display:

```text

|| Welcome to Geometric Calculator ||

Type 'help' for commands.

Type 'exit' to quit.

>

```

The `>` prompt means that the calculator is waiting for the next command.

The interface is intentionally REPL-like: the user enters one command, receives the result, and can then enter another command.

---

# 6. Understanding the REPL



The user directly enters Python-like commands.

For example:

```text

> p1 = Point(10, 10)

p1 created

```

The calculator creates a `Point` object and stores it under the name `p1`.

The user can then use the same object later:

```text

> p1.distance(p2)

```

This follows the interaction style shown in the assignment.

---

# 7. Creating Shapes

## Point

Create a point using:

```text

> p1 = Point(10, 10)

p1 created

```

Create another point:

```text

> p2 = Point(20, 20)

p2 created

```

The names `p1` and `p2` are chosen by the user.

---

## Line

A line uses two previously created points:

```text

> l1 = Line(p1, p2)

l1 created

```

The line can then be used for calculations.

---

## Circle

A circle requires a center point and radius:

```text

> c1 = Circle(Point(0, 0), 5)

c1 created

```

A previously created point can also be used as the center:

```text

> c2 = Circle(p1, 5)

c2 created

```

---

## Rectangle

The current rectangle representation uses two opposite corners:

```text

> r1 = Rectangle(Point(0, 0), Point(10, 10))

r1 created

```

Previously created points can also be used:

```text

> r1 = Rectangle(p1, p2)

r1 created

```

The current implementation assumes the rectangle is axis-aligned.

---

# 8. Calculating Shape Properties

## Point-to-Point Distance

Create two points:

```text

> p1 = Point(0, 0)

p1 created

> p2 = Point(3, 4)

p2 created

```

Then:

```text

> p1.distance(p2)

5.0

```

---

## Line Length

```text

> l1 = Line(p1, p2)

l1 created

> l1.length()

5.0

```

---

## Circle Area

```text

> c1 = Circle(Point(0, 0), 5)

c1 created

> c1.area()

78.53981633974483

```

---

## Circle Circumference

```text

> c1.circumference()

31.41592653589793

```

---

## Rectangle Area

```text

> r1 = Rectangle(Point(0, 0), Point(10, 5))

r1 created

> r1.area()

50.0

```

---

## Rectangle Perimeter

```text

> r1.perimeter()

30.0

```

---

# 9. Distance Between Shapes

The general distance function is:

```text

distance(shape1, shape2)

```

The calculator determines which two shape types were provided and performs the corresponding calculation.

## Point - Point

```text

> p1 = Point(0, 0)

p1 created

> p2 = Point(3, 4)

p2 created

> distance(p1, p2)

5.0

```

---

## Point - Line

```text

> p1 = Point(5, 5)

p1 created

> l1 = Line(Point(0, 0), Point(10, 0))

l1 created

> distance(p1, l1)

5.0

```

The reverse order is also supported:

```text

> distance(l1, p1)

5.0

```

---

## Point - Circle

```text

> p1 = Point(10, 0)

p1 created

> c1 = Circle(Point(0, 0), 5)

c1 created

> distance(p1, c1)

5.0

```

If the point is on or inside the circle, the distance is:

```text

0

```

---

## Point - Rectangle

```text

> p1 = Point(15, 5)

p1 created

> r1 = Rectangle(Point(0, 0), Point(10, 10))

r1 created

> distance(p1, r1)

5.0

```

If the point lies inside or on the rectangle boundary, the distance is:

```text

0

```

---

## Line - Line

```text

> l1 = Line(Point(0, 0), Point(10, 0))

l1 created

> l2 = Line(Point(0, 5), Point(10, 5))

l2 created

> distance(l1, l2)

5.0

```

---

## Line - Circle

```text

> l1 = Line(Point(0, 0), Point(10, 0))

l1 created

> c1 = Circle(Point(5, 5), 2)

c1 created

> distance(l1, c1)

3.0

```

If the line segment touches or intersects the circle, the distance is:

```text

0

```

---

## Line - Rectangle

```text

> l1 = Line(Point(0, 15), Point(10, 15))

l1 created

> r1 = Rectangle(Point(0, 0), Point(10, 10))

r1 created

> distance(l1, r1)

5.0

```

---

## Circle - Circle

```text

> c1 = Circle(Point(0, 0), 5)

c1 created

> c2 = Circle(Point(20, 0), 5)

c2 created

> distance(c1, c2)

10.0

```

If the circles touch or overlap, the distance is:

```text

0

```

---

## Circle - Rectangle

```text

> c1 = Circle(Point(15, 5), 2)

c1 created

> r1 = Rectangle(Point(0, 0), Point(10, 10))

r1 created

> distance(c1, r1)

3.0

```

If the circle touches or overlaps the rectangle, the distance is:

```text

0

```

---

## Rectangle - Rectangle

```text

> r1 = Rectangle(Point(0, 0), Point(10, 10))

r1 created

> r2 = Rectangle(Point(20, 0), Point(30, 10))

r2 created

> distance(r1, r2)

10.0

```

---

# 10. Using Previously Created Objects

Objects created during the session remain available through their names.

For example:

```text

> p1 = Point(0, 0)

p1 created

> p2 = Point(10, 0)

p2 created

> l1 = Line(p1, p2)

l1 created

```

Here, `l1` uses the already-created `p1` and `p2` objects.

The user can then continue using them:

```text

> p1.distance(p2)

10.0

> l1.length()

10.0

```

Objects are stored only for the duration of the current calculator session.

Restarting `main.py` starts with an empty object store.

---

# 11. Help Command

At any time, type:

```text

> help

```

The calculator displays the supported command format:

```text

Create shapes using:

p1 = Point(x, y)

l1 = Line(p1, p2)

c1 = Circle(center, radius)

r1 = Rectangle(p1, p2)

Calculate distance using:

distance(shape1, shape2)

```

---

# 12. Exiting

To close the calculator:

```text

> exit

Thanks!

```

The `exit` command stops the REPL loop.

---

# 13. Error Handling

Commands are executed inside a `try/except` block.

If an invalid command or unsupported operation is entered, the calculator prints an error instead of immediately terminating.

For example:

```text

> distance(p1, unknown_shape)

Error: ...

```

The calculator then returns to the prompt:

```text

>

```

The user can continue entering commands.

---

# 14. Design

The project follows a simple object-oriented structure.

Each geometric shape is represented by its own class.

```text

Point

  └── coordinates

Line

  ├── Point 1

  └── Point 2

Circle

  ├── Center

  └── Radius

Rectangle

  ├── Point 1

  └── Point 2

```

The distance calculations are kept separately in:

```text

distance_between_shapes.py

```

This keeps geometric data and calculations separated from the CLI.

The `main.py` file is responsible primarily for interaction with the user.

---

# 15. How the REPL Stores Objects

The calculator maintains an in-memory dictionary:

```python

objects = {}

```

When the user enters:

```text

> p1 = Point(10, 10)

```

the calculator effectively stores:

```text

"p1" → Point(10, 10)

```

After:

```text

> p2 = Point(20, 20)

```

the dictionary contains both:

```text

"p1" → Point(10, 10)

"p2" → Point(20, 20)

```

This allows later commands such as:

```text

> distance(p1, p2)

```

to access the previously created objects.

This storage is temporary and exists only while the program is running.

---

# 16. Assumptions

Some geometric details are not explicitly defined by the assignment. Where necessary, the following assumptions are used.

## Rectangle Representation

A rectangle is currently represented using two opposite corner points:

```text

Rectangle(p1, p2)

```

The rectangle is assumed to be axis-aligned.

For example:

```text

p1 = (0, 0)

p2 = (10, 10)

```

represents a rectangle whose sides are parallel to the x- and y-axes.

Rotated/inclined rectangles are not currently supported.

## Distance Definition

For two shapes, distance is interpreted as the minimum Euclidean distance between the shapes.

Therefore:

* touching shapes have distance `0`

* overlapping shapes have distance `0`

* separated shapes have a positive distance

For circles, for example, the distance is based on the gap between their boundaries rather than simply the distance between their centers.

These assumptions are documented because the assignment does not define a single exact representation or distance convention for every shape combination.

---



# 18. External Libraries

No external geometry library is used for the core calculations.

The geometric calculations are implemented directly in Python.

This keeps the implementation transparent and makes the mathematical logic easier to inspect and understand.

---

# 19. Development Approach

The project is developed incrementally.

The implementation is divided into small components:

1. Point

2. Line

3. Circle

4. Rectangle

5. Distance calculations

6. Interactive REPL

7. Error handling

8. Testing and improvements

9. Documentation

---