# Create a class called Person. Upon initialization, it will receive a name (str) and a surname (str).
# Implement the needed magic methods so that:
# •	Each person could be represented by their names, separated by a single space.
# •	When you concatenate two people, you should return a new instance of a person who will take the first name from
# the first person and the surname from the second person.
# Create another class called Group. Upon initialization, it should receive a name (str) and people
# (list of Person instances). Implement the needed magic methods so that:
# •	When you access the length of a group instance, you should receive the total number of people in the group.
# •	When you concatenate two groups, you should return a new instance of a group which will have a name-string in the
# format "{first_name} {second_name}" and all the people in the two groups will participate in the new one too.
# •	Each group should be represented in the format
# "Group {name} with members {members' names separated by comma and space}"
# •	You could iterate over a group, and each person (element of the group) should be represented in the format
# "Person {index}: {person's name}"
from typing import List


class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def __repr__(self) -> str:
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        if isinstance(other, Person):
            return Person(self.name, other.surname)


class Group:
    def __init__(self, name: str, people: List[Person]) -> None:
        self.name = name
        self.people: List[Person] = people

    def __len__(self) -> int:
        return len(self.people)

    def __add__(self, other):
        if isinstance(other, Group):
            group_name = f"{self.name} {other.name}"
            group_people = self.people + other.people
            return Group(group_name, group_people)

    def __repr__(self) -> str:
        return f"Group {self.name} with members {', '.join(str(p) for p in self.people)}"

    def __iter__(self):
        return iter(f'Person {index}: {p}' for index, p in enumerate(self.people))

    def __getitem__(self, index) -> str:
        return f'Person {index}: {self.people[index]}'
        # return next((v for i, v in enumerate(self.__iter__()) if i == index), None)


p0 = Person('Aleko', 'Dango')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)
