from point import Point
from line import Line
from circle import Circle
from rectangle import Rectangle
from distance_between_shapes import distance


objects = {}

print("|| Welcome to Geometric Calculator ||")
print("Type 'help' for commands.")
print("Type 'exit' to quit.")

while True:

    command = input("> ")

    if command == "exit":
        print("Thanks!")
        break

    elif command == "help":
        print("Create shapes using:")
        print("p1 = Point(x, y)")
        print("l1 = Line(p1, p2)")
        print("c1 = Circle(center, radius)")
        print("r1 = Rectangle(p1, p2)")
        print()
        print("Calculate distance using:")
        print("distance(shape1, shape2)")

    else:
        try:

            if "=" in command:

                name, expression = command.split("=", 1)

                name = name.strip()

                shape = eval(
                    expression.strip(),
                    {
                        "Point": Point,
                        "Line": Line,
                        "Circle": Circle,
                        "Rectangle": Rectangle
                    },
                    objects
                )

                objects[name] = shape

                print(name, "created")

            else:

                result = eval(
                    command,
                    {
                        "Point": Point,
                        "Line": Line,
                        "Circle": Circle,
                        "Rectangle": Rectangle,
                        "distance": distance
                    },
                    objects
                )

                print(result)

        except Exception as e:
            print("Error:", e)