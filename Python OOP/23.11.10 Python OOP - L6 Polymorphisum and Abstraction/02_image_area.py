# Create a class called ImageArea which will store the width and the height of an image.
# Create a method called get_area() which will return the area of the image.
# We have also to implement
# all the magic methods for the comparison of two image areas (>, >=, <, <=, ==, !=), which will compare their areas.

class ImageArea:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_area(self):
        return self.height * self.width

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    # def __gt__(self, other):
    #     return self.get_area() > other.get_area()
    #
    # def __ge__(self, other):
    #     return self.get_area() >= other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()


# test1
a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 == a2)
print(a1 != a3)
# True
# True

# Test 2
a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 != a2)
print(a1 >= a3)
# False
# False

# Test3:
a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 <= a2)
print(a1 < a3)
# True
# True
