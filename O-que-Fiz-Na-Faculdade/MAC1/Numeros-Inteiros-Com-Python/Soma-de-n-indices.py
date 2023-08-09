def somadentermos(n):
    if n == 0:
        return 0
    else:
        x = somadentermos(n-1)
        y = n + x
        return y
