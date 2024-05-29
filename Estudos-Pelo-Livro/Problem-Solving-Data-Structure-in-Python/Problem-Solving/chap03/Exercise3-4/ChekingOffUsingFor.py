# Com o uso do while fica melhor ainda

def anagramSolution1(s1,s2):
    
    if len(s1) != len(s2):
        return False
    
    else:
        s2 = list(s2)
              
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    s2[j] = None

        for l in s2:
            if l != None:
                return False
        return True

print(anagramSolution1('abcd','dcba'))
print(anagramSolution1('python','typhon'))
print(anagramSolution1('post','spot'))
print(anagramSolution1('listen','silent'))
print(anagramSolution1('race','care'))
print(anagramSolution1('persol','soldier'))
print(anagramSolution1('way','tea'))
print(anagramSolution1('raa','rae'))