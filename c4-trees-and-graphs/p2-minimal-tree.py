"""
[LeetCode] 108. Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: The resulting binary search tree is height-balanced, satisfying the problem's requirement.

Approach:
To build a height-balanced BST, we can use a recursive approach where the middle element of the sorted array becomes the root of the BST. 
The left half of the array will form the left subtree, and the right half will form the right subtree. 
This ensures the BST is balanced. 
We apply this logic recursively for each subtree.

Complexity Analysis:
- Time Complexity: O(N), where N is the number of elements in the array. Each element is visited exactly once to construct the BST.
- Space Complexity: O(log N) for the recursion stack. Though the output BST has O(N) space, the height of the tree (and thus the size of the call stack) is O(log N) since the tree is height-balanced.

"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return None

            # Middle element to maintain balance
            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            # Recursively build the left and right subtrees
            node.left = helper(left, mid - 1)
            node.right = helper(mid + 1, right)

            return node

        return helper(0, len(nums) - 1)


# Example usage
if __name__ == "__main__":
    sol = Solution()
    nums = [-10, -3, 0, 5, 9]
    tree_root = sol.sortedArrayToBST(nums)
    # Output: Binary tree root of a height-balanced BST created from nums
