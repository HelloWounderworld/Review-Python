import time
import random

def generate_anagram(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

base_word = 'a' * 100 + 'b' * 100 + 'c' * 100 + 'd' * 100 + 'e' * 100 + 'f' * 100 + 'g' * 100 + 'h' * 100 + 'i' * 100 + 'j' * 100 + 'k' * 100 + 'l' * 100 + 'm' * 100 + 'n' * 100

anagrams = [generate_anagram(base_word) for _ in range(2)]

def anagramSolution1(s1,s2):
    start = time.time()

    stillOK = True
    if len(s1) != len(s2):
        stillOK = False

    alist = list(s2)
    pos1 = 0

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    end = time.time()
    return stillOK, end - start

# print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution1('abcd','dcba'))
# print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution1('python','typhon'))
# print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution1('post','spot'))
# print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution1('listen','silent'))
# print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution1('race','care'))
# print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution1('persol','soldier'))
# print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution1('way','tea'))
# print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution1('raa','rae'))
print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution1(anagrams[0], anagrams[1]))
