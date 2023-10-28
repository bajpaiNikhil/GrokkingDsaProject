

# s = "abcde"
# words = ["a","bb","acd","ace"]
#
#
# left = 0
# right = len(s)
#
# def issubseq(t):
#     current_pos = -1
#     stack = []
#     for i in t:
#         if indices[i]:
#             pos = bisect.bisect_right(indices[i], current_pos)
#             if pos == len(indices[i]):
#                 return False
#             current_pos = indices[i][pos]
#         else:
#             return False
#     return True
#
#
# def check(s, words , mid):
#     count = 0
#     for i in words:
#         if s.
#
#
# while left<= right :
#     mid = left + (right - left) //2
#
#     if check(s , words,mid):
#         ans = mid
#         left = mid +1
#
#     else:
#         right = mid -1
