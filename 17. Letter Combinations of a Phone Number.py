
digits = "23"
digitsMapping = {
    1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"
}
combinationList = []

def backtrackingOnPhoneNumbers(path , index , digits , digitMapping):
    if len(path) == len(digits):
        combinationList.append("".join(path))
        return

    individualDigit = int(digits[index])
    for letter in digitsMapping[individualDigit]:
        path.append(letter)
        backtrackingOnPhoneNumbers(path , index+1,digits,digitMapping)
        path.pop()
backtrackingOnPhoneNumbers([],0,digits,digitsMapping)
print(combinationList)
# digits = "23"
# digitsMapping = {
#     1:"", 2: "abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"
# }
# combinationList = []
#
#
# def backTrack(index, path, digits, digitsMapping, combinationList):
#     if len(path) == len(digits):
#         combinationList.append(path)
#         return
#     digit = digits[index]
#     for letter in digitsMapping[digit]:
#         path+=letter
#         backTrack(index+1,path,digits,digitsMapping,combinationList)
#         path.removesuffix()
#
# backTrack(0,"",digits,digitsMapping,combinationList)
# print(combinationList)



