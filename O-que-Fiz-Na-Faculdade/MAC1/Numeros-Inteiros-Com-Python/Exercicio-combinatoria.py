def fatorial(n):
   prod = 1
   x = n
   while x > 0:
      prod = prod * x
      x = x - 1
   return prod
def Combinatoria(m,n):
   num = fatorial(m)
   demon = fatorial(n-m)*fatorial(m)
   return num / demon

def main():
   n = int(input("Entre com um valor de n:"))
   m = int(input("Entre com um valor de m:"))
   print("O valor e: C{},{}={}".format(n,m,Combinatoria(m,n)))
main()
