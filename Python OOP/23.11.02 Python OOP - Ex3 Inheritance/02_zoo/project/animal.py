# Follow the diagram and create all the classes. Except for the Animal class, each class should inherit from another
# class, as shown in the diagram. The Animal class should receive a name - string upon initialization.
# Every class should have a constructor, which accepts one parameter: name

class Animal:
    def __init__(self, name: str):
        self.name = name
