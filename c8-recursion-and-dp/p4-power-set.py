"""
[LeetCode]78. Subsets

Problem Statement:
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Approach:
Utilize a recursive depth-first search (DFS) method to explore every possible combination
of including or excluding each element in the subset. This method effectively generates all
subsets by traversing through each element's decision to be included in the current subset.

Complexity Analysis:
- Time Complexity: O(2^N), where N is the number of elements in the input array. This is because each element has two choices (either to be included or excluded), leading to 2^N possible subsets.
- Space Complexity: O(N), which is the space used by the recursion stack. While the total output space for all subsets is O(N*2^N), the space complexity for the function's execution excluding the output is O(N), determined by the depth of the recursion tree.

Solution:
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(index, path):
            res.append(path)
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return res


# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]
    print("All subsets:", solution.subsets(nums))
