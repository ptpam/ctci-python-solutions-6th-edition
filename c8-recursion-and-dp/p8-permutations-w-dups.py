"""
[LeetCode]47. Permutations II

Problem Statement:
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Examples:
1. Input: nums = [1,1,2]
   Output: [[1,1,2], [1,2,1], [2,1,1]]

2. Input: nums = [1,2,3]
   Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

Constraints:
- 1 <= nums.length <= 8
- -10 <= nums[i] <= 10

Approach:
The solution utilizes backtracking with a sorted input array to facilitate the identification of duplicates. To ensure only unique permutations are generated, we skip over duplicate elements by checking if the current element is the same as the previous one and whether the previous one has been visited in the current recursive call.

Complexity Analysis:
- Time Complexity: O(n*n!), where n is the number of elements in the input array. The sorting operation takes O(n log n), and generating permutations takes O(n!) time. However, due to the skipping of duplicates, the actual time may be less.
- Space Complexity: O(n), primarily due to the recursion stack and the visited set. This does not account for the space needed to store the result.

Solution Implementation:
"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort the array to make duplicate checking easier
        visited = (
            set()
        )  # Track visited indices to avoid reusing the same element in a permutation

        def backtracking(subset):
            if len(subset) == len(nums):
                res.append(subset[:])  # Append a copy of the current subset
                return

            for i in range(len(nums)):
                # Skip duplicates by checking if current is same as previous and previous was not visited
                if i in visited or (
                    i > 0 and nums[i] == nums[i - 1] and (i - 1) not in visited
                ):
                    continue
                visited.add(i)
                backtracking(
                    subset + [nums[i]]
                )  # Include nums[i] in the current permutation
                visited.remove(i)  # Backtrack

        backtracking([])
        return res


# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 2]
    print("Unique permutations:", solution.permuteUnique(nums))
