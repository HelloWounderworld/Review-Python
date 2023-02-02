def mdc(num,den):
    x = []
    y = []
    for i in range(1,num+1):
        if num%i == 0:
            x.append(i)
    for j in range(1,den+1):
        if den%i == 0:
            y.append(i)
    if len(x) <= len(y):
        z = []
        for i in range(len(y)):
            for j in range(len(x)):
                if y[i] == x[j]:
                    z.append(y[i])
        return max(z)
    else:
        z = []
        for i in range(len(x)):
            for j in range(len(y)):
                if x[i] == y[j]:
                    z.append(x[i])
        return max(z)
                    
