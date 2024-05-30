# import time
import random

def generate_anagram(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

base_word = 'a' * 100 + 'b' * 100 + 'c' * 100 + 'd' * 100 + 'e' * 100 + 'f' * 100 + 'g' * 100 + 'h' * 100 + 'i' * 100 + 'j' * 100 + 'k' * 100 + 'l' * 100 + 'm' * 100 + 'n' * 100

anagrams = [generate_anagram(base_word) for _ in range(4)]

def anagramSolution4(s1,s2):

    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        # ord - converte um caractere de uma string para um inteiro que representa-a
        # a - 97
        # b - 98
        # e assim sucessivamente
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True

    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK

# print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution4('apple','pleap'))
# print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution4('abcd','dcba'))
# print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution4('python','typhon'))
# print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution4('post','spot'))
# print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution4('listen','silent'))
# print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution4('race','care'))
# print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution4('persol','soldier'))
# print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution4('way','tea'))
# print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution4('raa','rae'))
# print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution4(anagrams[0], anagrams[1]))
# print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution4(anagrams[2], anagrams[3]))