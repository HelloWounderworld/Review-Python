import timeit
import importlib
import functools

def Timer(funcao_nome, modulo_nome, *args):
    if args == ():
        modulo = importlib.import_module(modulo_nome)

        funcao = getattr(modulo, funcao_nome)

        return funcao
    else:
        modulo = importlib.import_module(modulo_nome)

        funcao = getattr(modulo, funcao_nome)

        return functools.partial(funcao, *args)

# Exercise3-2
# print("Module Exercise3-2")
# sumGauss1 = Timer("sumOfN", "Exercise3-2.listing1-GaussSum", 1000000)
# print("Using for: ", timeit.timeit(sumGauss1, number = 1000), "milliseconds")
# sumGauss2 = Timer("sumOfNByGaussMethod", "Exercise3-2.listing1-GaussSum", 1000000)
# print("Using Gauss Expression: ", timeit.timeit(sumGauss2, number = 1000), "milliseconds")

# sumArquimediam1 = Timer("sumOfNSquareTerms", "Exercise3-2.listing-SumbySquareTerms", 1000000)
# print("Using for: ", timeit.timeit(sumArquimediam1, number = 1000), "milliseconds")
# sumArquimediam2 = Timer("sumOfNByGaussMethodSquareTerms", "Exercise3-2.listing-SumbySquareTerms", 1000000)
# print("Using using expression: ", timeit.timeit(sumArquimediam2, number = 1000), "milliseconds")

# sumCube1 = Timer("sumOfNCubicTerms", "Exercise3-2.SomaAoCubo", 1000000)
# print("Using for: ", timeit.timeit(sumCube1, number = 1000), "milliseconds")
# sumCube2 = Timer("sumOfArquimedesMethodsCubicTerms", "Exercise3-2.SomaAoCubo", 1000000)
# print("Using using expression: ", timeit.timeit(sumCube2, number = 1000), "milliseconds")

# Exercise3-3
# print()
# print("Module Exercise3-3")
# randomList = Timer("randomListGenerator", "Exercise3-3.minimumNumberOn")

# minimunNumberOn1 = Timer("minimumNumberOn", "Exercise3-3.minimumNumberOn", randomList())
# print("Using O(n): ", timeit.timeit(minimunNumberOn1, number = 1000), "milliseconds")

# minimunNumberOn2 = Timer("minimumNumberOn2", "Exercise3-3.minimumNumberOn2", randomList())
# print("Using O(n2): ", timeit.timeit(minimunNumberOn2, number = 1000), "milliseconds")

# Exercise3-4
# print()
# print("Module Exercise3-4")
# base_word = 'a' * 100 + 'b' * 100 + 'c' * 100 + 'd' * 100 + 'e' * 100 + 'f' * 100 + 'g' * 100 + 'h' * 100 + 'i' * 100 + 'j' * 100 + 'k' * 100 + 'l' * 100 + 'm' * 100 + 'n' * 100
# randomListAnagram = Timer("generate_anagram", "Exercise3-4.CheckingOff")
# anagrams = [randomListAnagram(base_word) for _ in range(2)]

# checkingOff1 = Timer("anagramSolution1", "Exercise3-4.CheckingOff", anagrams[0], anagrams[1])
# print("Using O(n2): ", timeit.timeit(checkingOff1, number = 1000), "milliseconds")

# checkingOff2 = Timer("anagramSolution4", "Exercise3-4.CountAndCompare", anagrams[0], anagrams[1])
# print("Using O(n): ", timeit.timeit(checkingOff2, number = 1000), "milliseconds")

# Exercise3.6
# print()
# print("Module Exercise3-6")
# t1 = Timer("test1", "Exercise3-6.FourDifferentWayToGenerateAList")
# print("concat ",timeit.timeit(t1, number=1000), "milliseconds")
# t2 = Timer("test2", "Exercise3-6.FourDifferentWayToGenerateAList")
# print("append ",timeit.timeit(t2, number=1000), "milliseconds")
# t3 = Timer("test3", "Exercise3-6.FourDifferentWayToGenerateAList")
# print("comprehension ",timeit.timeit(t3, number=1000), "milliseconds")
# t4 = Timer("test4", "Exercise3-6.FourDifferentWayToGenerateAList")
# print("list range ",timeit.timeit(t4, number=1000), "milliseconds")

popZero = Timer("PopTestZero", "Exercise3-6.popMethodCalculateVelocity")
print("Popzero ",timeit.timeit(popZero, number=100000), "milliseconds")
popEnd = Timer("PopTestEnd", "Exercise3-6.popMethodCalculateVelocity")
print("PopEnd ",timeit.timeit(popEnd, number=100000), "milliseconds")

# t1 = Timer("test1()", "from __main__ import test1")
# print("concat ",t1.timeit(number=1000), "milliseconds")
# t2 = Timer("test2()", "from __main__ import test2")
# print("append ",t2.timeit(number=1000), "milliseconds")
# t3 = Timer("test3()", "from __main__ import test3")
# print("comprehension ",t3.timeit(number=1000), "milliseconds")
# t4 = Timer("test4()", "from __main__ import test4")
# print("list range ",t4.timeit(number=1000), "milliseconds")