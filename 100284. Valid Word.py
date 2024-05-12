


def isValid(word):
    if len(word) < 3:
        return False
    for char in word:
        if not (char.isalpha() or char.isdigit()):
            return False
    vowelSet = set('aeiouAEIOU')
    has_vowel = False
    has_consonant = False
    for char in word:
        if char.isdigit():
            continue
        elif char in vowelSet:
            has_vowel = True
        else:
            has_consonant = True

    return has_vowel and has_consonant
words = "UuE6"
print(isValid(words))