"""
[LeetCode]22. Generate Parentheses

Problem Statement:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Examples:
1. Input: n = 3
   Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

2. Input: n = 1
   Output: ["()"]

Constraints:
- 1 <= n <= 8

Approach:
The solution uses a backtracking approach that involves adding an open parenthesis if we still have one left to add (open_n < n) and adding a close parenthesis if it won't exceed the number of open parentheses (close_n < open_n), thereby ensuring the generated parentheses are well-formed.

Complexity Analysis:
- Time Complexity: O(4^n / sqrt(n)), derived from the nth Catalan number, as there are C_n Catalan number of unique BSTs (Binary Search Trees), which is the same as the number of valid parentheses combinations.
- Space Complexity: O(n), where n is the maximum depth of the recursive call stack. This does not account for the space needed to hold the result.

Solution Implementation:
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(combination, open_n, close_n):
            # Base case: if the combination is complete
            if open_n == close_n == n:
                result.append(combination)
                return

            # If we can add an open parenthesis, do so
            if open_n < n:
                backtrack(combination + "(", open_n + 1, close_n)

            # If we can add a close parenthesis without surpassing open_n, do so
            if close_n < open_n:
                backtrack(combination + ")", open_n, close_n + 1)

        backtrack("", 0, 0)
        return result


# Example usage
if __name__ == "__main__":
    solution = Solution()
    n = 3
    print(
        "Well-formed parentheses combinations for n = 3:",
        solution.generateParenthesis(n),
    )
