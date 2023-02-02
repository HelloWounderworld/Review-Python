import sys

def main(argv = None):

    if argv == None:
        argv = sys.argv

    nome_programa = argv[0]
    
    argc = len(argv)    
    if argc != 4:
        mostre_uso(nome_programa)
        return

    try:
        n  = int(argv[1])
        re = float(argv[2])
        im = float(argv[3])
    except:
        mostre_uso(nome_programa)
        return
    
    c = complex(re, im)
    z = 0
    for t in range(n):
        print("z%d : %s, abs(z%d)=%2g"%(t, z, t, abs(z)))
        z = z*z + c

#----------------------------------------------------------------
def mostre_uso(nome_programa):
    msg = "prompt > python3 %s n re im\n"%nome_programa \
          + "            n  = número de iterações\n"  \
          + "            re = parte real de um número complexo\n"  \
          + "            im = parte imaginária de um número complexo"
    print(msg)
    
if __name__ == "__main__":
    main()
