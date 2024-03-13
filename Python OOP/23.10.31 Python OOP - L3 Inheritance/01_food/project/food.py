# In a folder called project create two files: food.py and fruit.py:
# •	In the food.py file, create a class called Food which will receive an expiration_date (str) upon initialization.
# •	In the fruit.py file, create a class called Fruit which will receive a name (str)
# and an expiration_date (str) upon initialization.
# Fruit should be inherited from Food.
# Submit in Judge a zip file of the folder project.

class Food:
    def __init__(self, expiration_date):
        self.expiration_date = expiration_date