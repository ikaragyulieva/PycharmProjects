# Create a class called vowels, which should receive a string.
# Implement the __iter__ and __next__ methods, so the iterator returns only the vowels from the string.
# Note: Submit only the class in the judge system

class vowels:
    def __init__(self, frase):
        self.frase = frase
        v = ['a', 'e', 'i', 'u', 'o', 'y']
        self.current_vowels = [l for l in self.frase if l.lower() in v]
        self.start = 0
        self.end = len(self.current_vowels) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration

        index = self.start
        self.start += 1
        return self.current_vowels[index]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
