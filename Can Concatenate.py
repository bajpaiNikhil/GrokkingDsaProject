"""
Write a function, canConcat, that takes in a string and an array of words as arguments. The function should return boolean indicating whether or not it is possible to concatenate words of the array together to form the string.

You may reuse words of the array as many times as needed.

test_00:
canConcat("oneisnone", ["one", "none", "is"]); // -> true
test_01:
canConcat("oneisnone", ["on", "e", "is"]); // -> false
test_02:
canConcat("oneisnone", ["on", "e", "is", "n"]); // -> true
test_03:
canConcat("foodisgood", ["is", "g", "ood", "f"]); // -> true
test_04:
canConcat("santahat", ["santah", "hat"]); // -> false
"""
l = []
def canCat(s,words,memo):
    if s in memo:
        return memo[s]
    if len(s) == 0:
        return True
    for word in words:
        if s[:len(word)] == word:
            suffix = s[len(word):]
            if canCat(suffix, words, memo):
                l.append(word)
                memo[suffix] = True
                return True
    memo[s] = False
    return False
s = "catsanddog"
words = ["cat","cats","and","sand","dog"]
print(canCat(s, words,{}))
print(l)



