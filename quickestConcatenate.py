"""
quickest concat
Write a function, quickestConcat, that takes in a string and an array of words as arguments. The function should return the minimum number of words needed to build the string by concatenating words of the array.

You may use words of the array as many times as needed.

test_00:
quickestConcat('caution', ['ca', 'ion', 'caut', 'ut']); // -> 2
test_01:
quickestConcat('caution', ['ion', 'caut', 'caution']); // -> 1
test_02:
quickestConcat('respondorreact', ['re', 'or', 'spond', 'act', 'respond']); // -> 4
test_03:
quickestConcat('simchacindy', ['sim', 'simcha', 'acindy', 'ch']); // -> 3

"""
import math


def quickestConcatenate(s,words):
    if len(s) == 0:
        return 0
    minWords = math.inf
    for word in words:
        if s[:len(word)] == word:
            suffix = s[len(word):]
            # print("2" ,minWords,suffix)

            attempt = 1+quickestConcatenate(suffix,words)
            # print("1" ,attempt,minWords,suffix)
            minWords = min(attempt,minWords)
    return minWords

print(quickestConcatenate('caution', ['ca', 'ion', 'caut', 'ut']))