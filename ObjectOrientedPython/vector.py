"""
Cameron Cheng
302738415
CS3035-01
vector.py overloads methods to work with the Vector class
"""
import math
class Vector:
    __a = 1
    __b = 1
    __c = 1

    """This is our Vector class which initializes our a,b,c variables to 1 if there 
    is a missing value for one of our variables
    
    """

    def __init__(self, a, b, c):
        """

        :param a: (int)
        :param b: (int)
        :param c: (int)
        """
        self.__a = a
        self.__b = b
        self.__c = c

    def __str__(self):
        """
        Overloaded string method

        :return:
            A string representation of the vector
        """

        return f'<{self.__a},{self.__b},{self.__c}>'

    def __repr__(self):
        """
        Overloaded repr method
        :return:
            A string representation of the vector
        """
        return f'Vector({self.__a},{self.__b},{self.__c})'

    def magnitude(self):
        """
        Method to find the magnitude of the entire vector
        :return:
            integer value of the magnitude of the vector
        """

        mag = math.sqrt(math.pow(self.__a,2) * math.pow(self.__b,2) * math.pow(self.__c,2))
        return mag

    def __eq__(self, other):
        """
        Overloaded equals comparison method
        :param other: 2nd vector to compare against the first vector
        :return: True if equal, False otherwise
        """

        v1 = Vector(self.__a, self.__b,self.__c)
        v2 = Vector(other.__a, other.__b, other.__c)

        if v1.__a == v2.__a and v1.__b == v2.__b and v1.__c == v2.__c:
            return True
        return False

    def __add__(self, other):

        """
        Overloaded addition method
        :param other: 2nd vector that is added to the first vector
        :return:
            a new vector with the values of the two vectors added together
        """

        v3 = Vector(self.__a + other.__a, self.__b + other.__b, self.__c + other.__c)

        return v3

    def __iadd__(self, other):
        """
        Overloaded += addition method
        :param other: 2nd vector
        :return:
            returns the first vector with the updated values after adding the 2nd
            vector to the first
        """

        v1 = Vector(self.__a + other.__a, self.__b + other.__b, self.__c + other.__c)

        return v1

    def __sub__(self, other):
        """
        Overloaded subtraction method

        :param other: 2nd vector to subtract from the first vector
        :return:
            returns a new vector with the values of the two vectors after subtraction
        """

        v3 = Vector(self.__a-other.__a, self.__b - other.__b, self.__c - other.__c)

        return v3

    def __isub__(self, other):
        """
        Overloaded -= subtraction method
        :param other: 2nd vector to subtract from the first vector
        :return:
            returns the first vector after subtracting the 2nd vector
        """

        v1 = Vector(self.__a - other.__a, self.__b - other.__b, self.__c - other.__c)

        return v1

    def __mul__(self, other):
        """
        Overloaded multiplication method
        :param other: second vector to multiply against the first
        :return:
            The multiplication of the two vectors or the scalar multiplication of the
            vector and the int
        """

        if isinstance(other, int):
            v1 = Vector(self.__a, self.__b, self.__c)

            v3 = Vector(v1.__a * other, v1.__b * other, v1.__c * other)

            return v3

        else:
            v1 = Vector(self.__a * other.__a, self.__b * other.__b, self.__c * other.__c)
            return v1

    def __rmul__(self, other):
        """
        Overloaded mutiplication method
        :param other: second vector to multiply against the first
        :return:
            The multiplication of the two vectors or the scalar multiplication of the
            vector and the int
        """
        if isinstance(other, int):

            v1 = Vector(self.__a, self.__b, self.__c)

            v2 = Vector(v1.__a * other, v1.__b * other, v1.__c * other)

            return v2
        else:
            v1 = Vector(self.__a * other.__a, self.__b * other.__b, self.__c * other.__c)
            return v1

    def __imul__(self, other):
        """
        Overloaded *= method
        :param other: int to multiply against the vector
        :return:
            returns the scalar multiplication of the vector and int
        """
        v1 = Vector(self.__a * other, self.__b * other, self.__c * other)
        return v1

    def __mod__(self, other):
        """
        Overloaded mod method
        :param other: second vector to cross multiply against the first vector
        :return:
            returns the cross product of the two vectors
        """
        v3 = Vector(self.__b * other.__c - self.__c * other.__b,
                    self.__c * other.__a - self.__a * other.__c,
                    self.__a * other.__b - self.__b * other.__a)

        return v3

    def __getitem__(self, item):
        """
        Overloaded get method
        :param item: int, to check the position of the item they want to get
        :return:
            returns the value at the index given as 'item"
        """
        if item == 0:
            return self.__a

        elif item == 1:
            return self.__b

        elif item == 2:
            return self.__c

    def __setitem__(self, key, value):
        """
        Overloaded setItem method
        :param key: (int) value to check which index is going to be changed
        :param value: (int) the value that the index is going to be changed to
        :return:
            returns the vector with the updated values
        """

        if key == 0:
            v3 = Vector(value, self.__b, self.__c)
            return v3
        elif key == 1:
            v3 = Vector(self.__a, value, self.__c)
            return v3
        elif key == 2:
            v3 = Vector(self.__a, self.__b, value)
            return v3





