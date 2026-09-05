from point import Point
from line import Line
from circle import Circle
from rectangle import Rectangle
from distance_between_shapes import distance
from three_dimension_calculation import Sphere, Cylinder, Cuboid


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

        print("2D Shapes:")
        print("p1 = Point(x, y)")
        print("l1 = Line(p1, p2)")
        print("c1 = Circle(center, radius)")
        print("r1 = Rectangle(p1, p2)")
        print()

        print("3D Shapes:")
        print("s1 = Sphere(x, y, z, radius)")
        print("cy1 = Cylinder(x, y, z, radius, height)")
        print("b1 = Cuboid(x, y, z, length, width, height)")
        print()

        print("2D Distance:")
        print("distance(shape1, shape2)")
        print()

        print("3D Calculations:")
        print("shape.surface_area()")
        print("shape.volume()")

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
                        "Rectangle": Rectangle,
                        "Sphere": Sphere,
                        "Cylinder": Cylinder,
                        "Cuboid": Cuboid
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
                        "distance": distance,
                        "Sphere": Sphere,
                        "Cylinder": Cylinder,
                        "Cuboid": Cuboid
                    },
                    objects
                )

                print(f"{result:.2f}")

        except Exception as e:
            print("Error:", e)