def twoFors(n):
    for i in range(n):
        for j in range(n):
            k = 2 + 2

def oneFor(n):
    for i in range(n):
        k = 2 + 2

def threeFors(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                k = 2 + 2

def threeForsParallels(n):
    for i in range(n):
        k = 2 + 2
    for j in range(n):
        k = 2 + 2
    for k in range(n):
        k = 2 + 2

def whilePerformance(n):
    i = n
    while i > 0:
        k = 2 + 2
        i = i // 2
