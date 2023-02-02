def fibonacchi(n):
    if n == 0 or n == 1:
        return 1
    else:       
        return fibonacchi(n-1)+fibonacchi(n-2)
