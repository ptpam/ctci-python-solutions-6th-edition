"""
[LeetCode]70. Climbing Stairs

Problem Statement:
You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Solutions:
1. Iterative Approach
2. Dynamic Programming with Memoization (Array)
3. Dynamic Programming with Memoization (Recursive)
4. Recursive Approach

Complexity Analysis:
- Time Complexity: O(n) for iterative and dynamic programming approaches, O(2^n) for the simple recursive approach.
- Space Complexity: O(n) for dynamic programming with memoization, O(1) for the iterative approach, and O(n) for the recursive call stack in the simple recursive approach.

Solution Implementation:
"""


class Solution:
    # Iterative Approach
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            one, two = one + two, one
        return one

    # Dynamic Programming with Memoization (Array)
    def climbStairs2(self, n: int) -> int:
        if n == 1:
            return 1
        memo = [0] * n
        memo[0], memo[1] = 1, 2
        for i in range(2, n):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n - 1]

    # Dynamic Programming with Memoization (Recursive)
    def climbStairs3(self, n: int) -> int:
        if n == 1:
            return 1
        memo = [-1] * n
        memo[0], memo[1] = 1, 2

        def helper(a):
            if memo[a] < 0:
                memo[a] = helper(a - 1) + helper(a - 2)
            return memo[a]

        return helper(n - 1)

    # Recursive Approach
    def climbStairs4(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        return self.climbStairs4(n - 1) + self.climbStairs4(n - 2)


# Example usage
if __name__ == "__main__":
    solution = Solution()
    n = 5  # Example input
    print(f"Solution 1: {solution.climbStairs(n)}")  # Iterative Approach
    print(f"Solution 2: {solution.climbStairs2(n)}")  # DP with Memoization (Array)
    print(f"Solution 3: {solution.climbStairs3(n)}")  # DP with Memoization (Recursive)
    print(f"Solution 4: {solution.climbStairs4(n)}")  # Recursive Approach
