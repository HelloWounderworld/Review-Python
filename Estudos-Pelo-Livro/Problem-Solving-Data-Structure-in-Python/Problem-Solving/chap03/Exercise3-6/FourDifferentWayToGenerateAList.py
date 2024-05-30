# Four different ways we might generate a list of numbers

# import time

def test1():

    l = []
    for i in range(10000):
        l = l + [i]

def test2():

    l = []
    for i in range(10000):
        l.append(i)

def test3():
    l = [i for i in range(10000)]

def test4():
    l = list(range(10000))

# print('is anagram: %s. Time cost: %10.20f seconds'%test1())
# print('is anagram: %s. Time cost: %10.20f seconds'%test2())
# print('is anagram: %s. Time cost: %10.20f seconds'%test3())
# print('is anagram: %s. Time cost: %10.20f seconds'%test4())

# print('Time cost: %10.20f seconds'%test1())
# print('Time cost: %10.20f seconds'%test2())
# print('Time cost: %10.20f seconds'%test3())
# print('Time cost: %10.20f seconds'%test4())