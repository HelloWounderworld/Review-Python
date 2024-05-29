import time
import random

def generate_anagram(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

base_word = 'a' * 100 + 'b' * 100 + 'c' * 100 + 'd' * 100 + 'e' * 100 + 'f' * 100 + 'g' * 100 + 'h' * 100 + 'i' * 100 + 'j' * 100 + 'k' * 100 + 'l' * 100 + 'm' * 100 + 'n' * 100

anagrams = [generate_anagram(base_word) for _ in range(2)]

def anagramSolution2(s1,s2):
    start = time.time()
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    end = time.time()
    return matches, end - start

# print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution2('abcd','dcba'))
# print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution2('python','typhon'))
# print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution2('post','spot'))
# print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution2('listen','silent'))
# print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution2('race','care'))
# print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution2('persol','soldier'))
# print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution2('way','tea'))
# print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution2('raa','rae'))
print('is anagram: %s. Time cost: %10.20f seconds'%anagramSolution2(anagrams[0], anagrams[1]))