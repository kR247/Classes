class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        name = args[0]
        cls.houses_history.append(name)
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесен, но он остался в истории')

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
            self.number_of_floors = x + y
            return self

    def __radd__(self, value):
        self.number_of_floors = self.number_of_floors.__add__(value)
        return self

    def __iadd__(self, value):
        self.number_of_floors += value
        return self


h1 = House('ЖК Эльдорадо', 25)
print(House.houses_history)
h2 = House('ЖК Эдем', 30)
print(House.houses_history)
h3 = House('ЖК Нарния',20)
print(House.houses_history)
del h2
del h3
print(House.houses_history)
del h1
print(House.houses_history)