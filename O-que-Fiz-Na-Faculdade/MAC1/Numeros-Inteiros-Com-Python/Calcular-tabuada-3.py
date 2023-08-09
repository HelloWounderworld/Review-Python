def main():
    n = int(input("Entre com uma valor de n:"))
    x = 1
    while x <= n:
        y = 1
        while y <= n:
            print(x, "x", y, "=", x * y)
            y = y + 1
        x = x + 1
main()
