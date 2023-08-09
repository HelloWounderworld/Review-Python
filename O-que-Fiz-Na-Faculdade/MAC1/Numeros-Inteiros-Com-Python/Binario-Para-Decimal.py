def binarioParaDecimal():
    decimal = 0
    pot = 1
    while (n > 0):
        digito = n % 10
        print("Mostre-me o processo: ", digito)
        decimal = decimal + digito * pot
        print("Revele o Processo: ", decimal)
        pot = pot * 2
        n = n // 10
    return decimal

def main():
    b = int(input("Entre com o numero na base 2: "))
    d = binarioParaDecimal(b)
    print("O valor {} na base 2 representa {} na base 10". format(b,d))
main()
