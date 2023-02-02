def is_prime(n):
    if n>3:
        divide = 2
        primo = True
        while n>divide and primo == True:
            if n%divide == 0:
                primo = False
            divide = divide + 1
    elif n>1:
        return True
    else:
        return False
    return primo
