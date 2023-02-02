#
# Conversor de número decimais para binarios
# usando append() e pop() de lista 
# 

PROMPT = "base 10 >>> "
QUIT = ''

def main():
    '''
    Recebe uma string e verifica se a substring formada apenas dos
    parênteses, colchetes e chaves da string é bem formada.
    '''
    print("Conversor de decimal para binário.")
    print("[Tecle ENTER para encerrar o programa.]")

    decimal_str = input(PROMPT)
    while decimal_str != QUIT:
        decimal = int(decimal_str)
        print("base 2:    ", to_string2(decimal))
        decimal_str = input(PROMPT)

#-------------------------------------------------------        
def to_string2(dec):
    ''' (int) -> str

    Recebe um número inteiro e retorna uma string que representa
    o número na base 2.
    '''
    if dec == 0: return '0'
    bin_str = ''
    pilha = []
    negativo = False
    if dec < 0:
        negativo = True
        dec = -dec

    # determine os dígitos de dec na base 2    
    while dec > 0:
        dig_2 = dec % 2
        pilha.append(dig_2)
        dec //= 2

    # converta os dígitos para str
    while pilha != []:
        dig_str  = str(pilha.pop())
        bin_str += dig_str

    if negativo: bin_str = "-" + bin_str
    return bin_str

#--------------------------------------------
if __name__ == "__main__":
    main()      
