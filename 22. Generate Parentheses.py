def backTrackFunc(n, leftCount, rightCount, result, output):
    """
    Recursively generates valid parentheses combinations using backtracking.

    - Base case: If both leftCount and rightCount reach `n`, a valid sequence is added.
    - Recursive step:
      - Add `(` if leftCount < n.
      - Add `)` if rightCount < leftCount to maintain validity.
      - After recursion, remove the last character to backtrack.
    """

    if leftCount >= n and rightCount >= n:  # Base case: Valid combination formed
        output.append("".join(result))
        return

    if leftCount < n:  # Add '(' if not exceeding `n`
        result.append("(")
        backTrackFunc(n, leftCount + 1, rightCount, result, output)
        result.pop()  # Backtrack: remove last added '('

    if rightCount < leftCount:  # Add ')' only if there's an unmatched '('
        result.append(")")
        backTrackFunc(n, leftCount, rightCount + 1, result, output)
        result.pop()  # Backtrack: remove last added ')'


# Example usage
n = 3
result = []
output = []
backTrackFunc(n, 0, 0, result, output)
print(output)  # Expected output: ['((()))', '(()())', '(())()', '()(())', '()()()']
