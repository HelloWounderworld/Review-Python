# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return


gen = generator(maximum=1000000)
# print(gen)
# print(gen.__iter__())
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
for n in gen:
    if n == 20:
        print('Calmou e parou!!!')
        break
    print(n)

# def generator(n=0):
#     yield 1
#     print('Continuando......')
#     yield 2

# gen = generator(n=0)
# # print(gen.__iter__())
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))

# for n in gen:
#     print(n)