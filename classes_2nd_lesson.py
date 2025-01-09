class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor <= self.number_of_floors:
            a = list(range(1, int(new_floor + 1)))
            for i in a:
                print(i)
        else:
            print('Такого этажа не сущестувует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):

        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            if isinstance(other.number_of_floors, int):
                return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            if isinstance(other.number_of_floors, int):
                return self.number_of_floors < other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, House):
            if isinstance(other.number_of_floors, int):
                return self.number_of_floors > other.number_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            if isinstance(other.number_of_floors, int):
                return self.number_of_floors <= other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            if isinstance(other.number_of_floors, int):
                return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            if isinstance(other.number_of_floors, int):
                return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            x = self.number_of_floors
            y = value
            return x + y

    def __radd__(self, value):
        y = self.number_of_floors
        x = value
        return x.__add__(y)






h1 = House('Эльдорадо', 25)
h2 = House('Эдем', 30)

h1.go_to(15)
h2.go_to(32)

print(h1)
print(h2)
print(len(h1))
print(len(h2))

print(h1 + 10)  # __add__
print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
print(11 + h1)  # __radd__


