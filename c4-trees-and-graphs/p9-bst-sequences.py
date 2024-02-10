"""
[LettCode]1569. Number of Ways to Reorder Array to Get Same BST

Problem Statement:
Given an array nums that represents a permutation of integers from 1 to n. 
We are going to construct a binary search tree (BST) by inserting the elements of nums in order into an initially empty BST. 
The task is to find the number of different ways to reorder nums so that the constructed BST is identical to that formed from the original array nums.

Example:
Input: nums = [2,1,3]
Output: 1
Explanation: There is only one way to reorder nums ([2,3,1]) that yields the same BST as the original BST formed from nums. 
Other reorderings like [3,2,1] yield different BSTs.

Approach:
1. The key is to understand that the structure of a BST is determined by the order of elements relative to each other, not their absolute positions in the array.
2. Use recursion to split the problem into subproblems based on the root of the BST. The root divides the remaining numbers into those less than the root (forming the left subtree) and those greater than the root (forming the right subtree).
3. The number of ways to reorder the BST is determined by the number of ways to reorder the left and right subtrees independently, multiplied together, and then multiplied by the number of ways to interleave these two subtrees while maintaining their internal order.
4. Use dynamic programming or memoization to calculate combinations efficiently and to avoid recalculating for the same subtree sizes.

Complexity Analysis:
- Time Complexity: O(N^2), where N is the number of elements in nums. The complexity arises from recursively processing each subset of the array and calculating combinations.
- Space Complexity: O(N^2) for storing intermediate results and the recursion stack.

Solution:
"""

from typing import List
from math import comb

MOD = 10**9 + 7


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def countWays(nums):
            if len(nums) <= 1:
                return 1
            leftSubtree = [x for x in nums if x < nums[0]]
            rightSubtree = [x for x in nums if x > nums[0]]

            leftWays = countWays(leftSubtree)
            rightWays = countWays(rightSubtree)

            # Calculate ways to interleave left and right subtrees
            totalWays = (
                comb(len(leftSubtree) + len(rightSubtree), len(leftSubtree))
                * leftWays
                * rightWays
            )
            return totalWays % MOD

        return (
            countWays(nums) - 1
        ) % MOD  # Subtract 1 to exclude the original ordering


# Example usage
if __name__ == "__main__":
    sol = Solution()
    nums = [2, 1, 3]
    print(sol.numOfWays(nums))  # Output: 1
