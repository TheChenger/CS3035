"""
Cameron Cheng

CS3035-01
main.py is the driver of the program, it asks users how many
cylinders and pyramids they'd like to create and then shows
that all the methods in the shapeList work properly
"""
import doctest
import random

import shape3d
import cylinder
import pyramid
import shape_list

def main():


    num_of_cylinders = input("Enter the amount of cylinders to create: ")
    num_of_pyramids = input("Enter the amount of pyramids to create: ")

    listOfShapes = shape_list.ShapeList()
    listOfColors = ["black", "maroon", "brown", "olive", "teal",
                    "navy", "red", "orange", "lime", "green",
                    "cyan", "blue", "purple", "magenta", "grey",
                    "pink", "apricot", "beige", "mint", "lavender"]

    for i in range(int(num_of_cylinders)):
        shape = cylinder.Cylinder(color=listOfColors[random.randint(0, 19)],
                                  transparency=round(random.uniform(0.00, 1.00), 2),
                                  radius= round(random.uniform(0.00, 50.00), 2),
                                  height= round(random.uniform(0.00, 50.00), 2))
        listOfShapes.append(shape)

    for i in range(int(num_of_pyramids)):
        shape = pyramid.Pyramid(color=listOfColors[random.randint(0, 19)],
                                transparency=round(random.uniform(0.00, 1.00), 2),
                                base= round(random.uniform(0.00, 50.00), 2),
                                height= round(random.uniform(0.00, 50.00), 2),
                                slant= round(random.uniform(0.00, 50.00), 2))
        listOfShapes.append(shape)

    random.shuffle(listOfShapes)

    listOfShapes.display_cylinders()
    print(listOfShapes.average_area_of_cylinders())
    listOfShapes.display_pyramids()
    print(listOfShapes.average_area_of_pyramids())
    print(listOfShapes.max_volume())
    print(listOfShapes.min_volume())


if __name__ == "__main__":
    main()
    doctest.testmod()