"""
Coin Change II

Problem Statement:
Given an array of integers representing coin denominations and an integer representing a total amount of money, return the number of combinations that make up that amount. If no combination of the coins can make up the amount, return 0. Assume an infinite number of each kind of coin is available.

Example:
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: There are four ways to make up the amount:
- 5 = 5
- 5 = 2 + 2 + 1
- 5 = 2 + 1 + 1 + 1
- 5 = 1 + 1 + 1 + 1 + 1

Approach:
The solution uses a recursive approach with memoization. We explore two scenarios for each coin: including it in the current combination or skipping it to try the next coin. The memoization cache is indexed by the current coin's index and the remaining amount to avoid recalculating the results of subproblems.

Complexity Analysis:
- Time Complexity: O(m*n), where m is the total amount and n is the number of coin denominations. This is due to iterating over each coin for amounts up to m.
- Space Complexity: O(m*n) for the memoization cache, plus O(n) for the recursion stack, leading to a total of O(m*n).

Solution Implementation:
"""

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Memoization cache to store the number of ways to make up amounts using subsets of coins
        cache = {}

        def dfs(i, a):
            # Base cases
            if a == amount:
                return 1
            elif i == len(coins) or a > amount:
                return 0
            # Check cache to avoid recomputation
            if (i, a) in cache:
                return cache[(i, a)]

            # Compute the number of combinations by including the current coin or skipping it
            cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            return cache[(i, a)]

        return dfs(0, 0)


# Example usage
if __name__ == "__main__":
    solution = Solution()
    amount = 5
    coins = [1, 2, 5]
    print("Number of combinations:", solution.change(amount, coins))
