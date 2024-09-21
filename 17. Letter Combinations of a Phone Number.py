
digits = "23"
digitsMapping = {
    1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"
}
combinationList = []

def backTrack(index, path, digits, digitsMapping, combinationList):
    if len(path) == len(digits):
        combinationList.append("".join(path))
        return
    digit = int(digits[index])
    for letter in digitsMapping[digit]:
        path.append(letter)
        backTrack(index + 1, path, digits, digitsMapping, combinationList)
        path.pop()

backTrack(0, [], digits, digitsMapping, combinationList)
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
