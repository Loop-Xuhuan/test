# class: blueprint for creating new object: Human
# object: instance of class (类的实例): John, Mary, Jack
# self is the reference to the current object
# cls is the reference to the class

class Point:
    default_color = 'red'

    __slots__ = ('x_axis', 'y_axis')  # 这个属性定义在类里，是一个元组，规定对象可以存在的属性

    def __init__(self, x, y):   # constructor: executed when we create a new point object
        self.x_axis = x
        self.y_axis = y

    def __str__(self):
        return f"({self.x_axis}, {self.y_axis})"

    def __eq__(self, other):
        return self.x_axis == other.x_axis and self.y_axis == other.y_axis

    def __add__(self, other):
        return Point(self.x_axis + other.x_axis, self.y_axis + other.y_axis)

    @classmethod
    def zero(cls):
        return cls(0, 0)   # same as calling Point(0, 0)

    def draw(self):
        print(f"Point ({self.x_axis}, {self.y_axis})")


point = Point(1, 2)
print(point.x_axis, point.y_axis)
point.draw()
# instance attributes
point.x_axis = 5
print(point.x_axis, point.y_axis)
point.draw()
# class attributes - shared across all instance of a class
print(point.default_color)
point.default_color = 'blue'
print(point.default_color)
# class methods
point = Point.zero()
point.draw()
# __str__: convert an object to a string
print(point)   # the default implementation str method of point object
print(point.__str__())
# __eq__: 如果没有__eq__, object比较的是两个object的内存地址是否相等
point1 = Point(1, 2)
point2 = Point(1, 2)
print(point1 == point2)
print(point1.__eq__(point2))
# __add__
print(point1 + point2)
print(point1.__add__(point2))


# making custom container
class TagClound:
    def __init__(self):
        self.__tags = {}   # __tags is a private member, makes this attribute private

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagClound()
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud["python"])   # __getitem__
cloud["java"] = 5   # __setitem__
print(len(cloud))   # __len__
for tag in cloud:
    print(tag)
print(cloud.__dict__)


# properties
class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value


product = Product(10)
print(product.get_price())


class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    price = property(get_price, set_price)


product = Product(10)
product.price = 20
print(product.price)


class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value


product = Product(50)
product.price = 20
print(product.price)


# inheritance
class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")


# Animal: Parent, Base
# Mammal: Child, Sub
class Mammal(Animal):
    def __init__(self):
        print("Mammal Constructor")
        self.weight = 2
        super().__init__()  # method overwriting，直接调用父类方法

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


fish1 = Fish()
m = Mammal()
fish1.eat()  # inherent method
print(fish1.age)  # inherent attribute
print(isinstance(fish1, Fish))
print(isinstance(fish1, Animal))
print(isinstance(fish1, object))
print(issubclass(Mammal, Animal))
print(issubclass(Animal, object))
# method overwriting，先寻找自己class的method，然后寻找第一个base，第二个base。。。
# 如class Manager(Person, Employee): 先在Manager中找method，然后Person然后Employee
print(m.age)
print(m.weight)


# an example
from abc import ABC, abstractclassmethod

class InvalidOperationError(Exception):
    pass


class Stream(ABC):  # ABC使Stream变成 abstract class，无法实例化
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False

    @abstractclassmethod  # 这个装饰器使得所有的sub class必须有read，否则就是abstract class
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


def read(streams):
    for stream in streams:
        stream.read()


stream1 = FileStream()
stream2 = NetworkStream()
read([stream1, stream2])


