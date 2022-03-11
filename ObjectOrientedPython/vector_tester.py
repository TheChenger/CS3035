"""
Cameron Cheng
302738415
CS3035-01
vector_tester.py tests each overloaded method
https://calstatela.instructuremedia.com/embed/27562c11-1374-4c3f-8541-70d819cf1ea0
"""
import doctest

from vector import Vector

def main():
    vect1 = Vector(1,2,3)
    vect2 = Vector(4,5,6)
    vect3 = Vector(7,8,9)
    vect4 = Vector(1,2,3)

    print("String representation of vect1: ")
    print(vect1)
    print()
    print("String representation of vect2 but using the repr method: ")
    print(repr(vect2))
    print()
    print("The magnitude of vector <7,8,9> ")
    print(vect3.magnitude())
    print()
    print("Comparing vect1 to vect: 2")
    print(vect1 == vect2)
    print()
    print("Adding vect1 and vect2: ")
    print(vect1 + vect2)
    print()
    print("Adding vect2 to vect1 and returning vect1: ")
    vect1 += vect2
    print(vect1)
    print()
    print("Subtracting vect3 from vect2: ")
    print(vect2 - vect3)
    print()
    print("Subtracting vect2 from vect1 and returning vect1: ")
    vect1 -= vect2
    print(vect1)
    print()
    print("Multiplication of vect1 and vect2: ")
    print(vect1 * vect2)
    print()
    print("Scalar multiplication of vect1 and 3: ")
    vect1 *= 3
    print(vect1)
    print()
    print("Print the cross product of vect4 and vect3: ")
    print(vect4 % vect3)
    print()
    print("The value of vect4 at index 2: ")
    print(vect4[2])
    print()
    print("Replaces the value of index 2 with the value of 9")
    print(vect4.__setitem__(2,9))
    print()

if __name__ == "__main__":
    main()
    doctest.testmod()

