# Create a class called dictionary_iter. Upon initialization, it should receive a dictionary object.
# Implement the iterator to return each key-value pair of the dictionary as a tuple of two elements
# (the key and the value).
# Note: Submit only the class in the judge system


class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dict = tuple(dictionary.items())
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= len(self.dict):
            raise StopIteration()
        index = self.start
        self.start += 1
        return self.dict[index]


# Tests:
result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
