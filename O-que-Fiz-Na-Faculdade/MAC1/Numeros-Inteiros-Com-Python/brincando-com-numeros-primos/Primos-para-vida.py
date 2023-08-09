'''Preciso pensar numa forma que pegue os numeros primos ja encontrados e ver se nao existe alguma forma de verificar se nap existe algum
   outro numero primo entre dos numeros primos ja conhecidos'''

'''Primeiro preciso encontrar alguma forma que otimize os calculos que de fatoriais ou numeoros de casas extremamente maiores'''

'''Segundo lugar, usando listas, tentar verificar se existe algum outro numero primo entre dos numeros primos ja conhecidos'''

'''Terceiro, desenvolver algum programa que consiga encontrar de maineira mais otimista um outro numero primo e usar o programa da segunda
   para verificar se nao ha algum outro numero primo entre eles'''

def main():
    n = int(input("Entre com um número primo: "))
    x = n-1
    prod = 1
    while (x < 0):
        prod = prod*x
        x = x-1
    y = prod + 1
    A = []
    while(y%n != 0):
        
        
        
    
