def mdc(n,m):
    n1 = max(n,m)
    n2 = min(n,m)
    while n1%n2 != 0:
        n3 = n2
        n2 = n1%n2
        n1 = n3
    return n2
