def é_par(n):
    if n % 2 == 0:
        print("é par: ", n)
        
    else:
        print("é ímpar: ", n)
    return print
print(é_par(10), True)
print(é_par(5), False)
print(é_par(1), False)
print(é_par(0), True)
