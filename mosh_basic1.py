import math
from collections import deque
from functools import reduce

# Formatted Strings
# can put any valid expression between {}
first = 'Xuhuan'
last = 'Wang'
age = 19
money = 3.14
print(f"{first} {last}")
print('大家好，我的名字是%s，我今年%d岁了，我今天挣了%.2f元钱' % (first, age, money))

# String methods
course = "Python Programming"
print(course.upper())
print(course)
print(course.lower())
print(course.find('Pro'))
print(course.replace('p', 'j'))
print('pro' in course, 'Pro' in course, 'swift' not in course)
print(course.split(sep=' '))  # split方法可以将一个字符串切割成一个列表
file_name = '2020.2.14拍摄.mp4'
print(file_name.rpartition('.'))  # 获取文件名和后缀名

# Numbers
x = 10
x = x + 3
x += 3
print(round(2.9))
print(abs(-2.9))
print(math.ceil(2.2))

# Type Conversion
# int(x)
# float(x)
# bool(x) -- False: '', 0, None
# str(x)
x = int(input("x: "))
y = x + 1
print(f"x: {x}, y: {y}")

# Flow Control
# Ternary Operator
age = 12
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

# Logical Operator
high_income = True
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")

# For Else
# 只有for loop被early terminate/break才不会执行else后的语句
successful = True
for i in range(0, 10, 2):
    print("Attempt", i)
    if successful:
        print("Successful")
        break
else:
    print("Attempted 5 times but failed")


# Functions
# 1- Perform a task


def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet("Xuhuan", "Wang")


# 2- Return a value


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Xuhuan")
print(message)


# *args


def multiply(*numbers):
    print(numbers)  # it's saved in tuples
    total = 1
    for i in numbers:
        total *= i
    return total


print(multiply(2, 3, 4, 5))


# **kwargs


def save_user(**user):
    print(user)  # it's saved in dict
    print(user['name'])


save_user(id=1, name="John", age=22)

# Data Structure
# List
numbers = [1, 2, 3, 4, 4, 4, 9]
fst, *others, lst = numbers
print(fst, lst, others)
print(numbers)

letters = ['a', 'b', 'c']
for index, i in enumerate(letters):
    print(index, i)

# Add
letters.append('d')
print(letters)
letters.insert(0, "-")
print(letters)

# Remove
letters.pop()  # remove the last one
letters.pop(0)
letters.remove('b')  # remove the first 'b'
del letters[0]

letters.index('c')
letters.count('c')

# Sort
numbers = [3, 51, 2, 8, 6]
numbers.sort(reverse=True)
numbers1 = sorted(numbers)
print(numbers, numbers1)

items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)  # 这里引用的是函数对象，没有调用函数(不需要结果)
print(items)
# lambda
items.sort(key=lambda item: item[1])  # same as sort_item function

# map
x = map(lambda item: item[1], items)
print(x)
for i in x:
    print(i)
# you can pass any iterables to list function to create a new list
y = list(map(lambda item: item[1], items))
print(y)

# filter function: 对可迭代对象进行过滤，得到一个filter对象，也是一个可迭代对象
x = filter(lambda item: item[1] >= 10, items)
print(x)
filtered = list(x)
print(filtered)

# reduce
print(reduce(lambda x, y: x + y[1], items, 0))

# list comprehensions
prices = [item for item in items if item[1] >= 10]

# zip function
list1 = [1, 2, 3]
list2 = [10, 20, 30]

list_combined = list(zip('abc', list1, list2))
print(list_combined)

# stacks - LIFO
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
lst = browsing_session.pop()

# queue - FIFO
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()

# tuples
x = 1, 2, 3  # the same as (1, 2, 3)
print(type(x))
x, y = 5, 7  # tuple assignment
print(x, y)

# dictionary
point1 = {'x': 1, 'y': 2}
point = dict(x=1, y=2)
del point['x']

for key, value in point.items():
    print(key, value)

point2 = {v: k for k, v in point1.items()}
print(point2)
# 字典的合并用update，dict1.update(dict2)；list合并可以相加，或者list1.extend(list2)

# generator object: save a lot of memories
value = (x * 2 for x in range(5))
print(value)
for i in value:
    print(i)

# unpacking operator - can unpack any iterable
numbers = [1, 2, 3]
print(*numbers)
print([*range(5), *"Hello World"])

# Exceptions
# else只有在没有exception时才会执行，类似于for else
# finally可用于释放外部资源，可以用在最后无论如何都会被执行
try:
    file = open("exercise.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError) as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
except ZeroDivisionError:
    print("Age cannot be 0")
else:
    print("No exceptions were throw.")
finally:  # will always be executed whether we have an exception or not
    file.close()

# with statement
try:
    with open("exercise.py") as a, open("string_encrypt.py") as b:
        print("File opened, and closed automatically")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError) as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
except ZeroDivisionError:
    print("Age cannot be 0")
else:
    print("No exceptions were throw.")


# raise exceptions
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


# eval: 可执行字符串中的代码
a = 'input("请输入您的用户名")'
eval(a)


# 相对路径：当前文件所在的文件夹开始的路径
# ../ 表示返回到上一级文件夹
# ./ 表示当前文件夹
file = open('test.txt')
print(file.read())
file.close()
