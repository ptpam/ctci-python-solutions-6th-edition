"""
[LeetCode]46. Permutations

Problem Statement:
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Examples:
1. Input: nums = [1,2,3]
   Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
2. Input: nums = [0,1]
   Output: [[0,1], [1,0]]
3. Input: nums = [1]
   Output: [[1]]

Approach:
Use backtracking to generate all possible permutations. A `visited` set is used to track which elements are currently included in the permutation being constructed to avoid duplicates.

Complexity Analysis:
- Time Complexity: O(N!), where N is the number of integers in the input array. This accounts for the fact that there are N! possible permutations.
- Space Complexity: O(N), where N is the number of integers in the input array. This space is used to maintain the call stack for recursive calls and does not account for the output space.

Solution Implementation:
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()  # Track visited indices

        def backtracking(subset):
            # Base case: if the subset length equals nums length, add it to result
            if len(subset) == len(nums):
                res.append(subset[:])  # Use subset[:] to add a copy of subset
                return

            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)  # Mark the current element as visited
                    subset.append(nums[i])  # Include nums[i] in the current permutation
                    backtracking(subset)  # Continue to build the permutation
                    visited.remove(
                        i
                    )  # Backtrack: remove nums[i] from visited for the next iteration
                    subset.pop()  # Remove the last element added to subset for backtracking

        backtracking([])  # Start backtracking with an empty subset
        return res


# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]
    print("All permutations:", solution.permute(nums))
