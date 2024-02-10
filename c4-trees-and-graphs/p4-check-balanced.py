"""
[LeetCode]110. Determine if a Binary Tree is Height-Balanced

A binary tree is height-balanced if for every node in the tree, the difference between the heights of the left subtree and the right subtree is no more than one.

Example:
Input: root = [3,9,20,null,null,15,7]
Output: true
Explanation: The given binary tree is height-balanced. The depths of the left and right subtrees of all nodes differ by no more than 1.

Approach:
The strategy to solve this problem involves a bottom-up traversal of the tree. At each node, we calculate the height of its left and right subtrees. If the difference in heights is more than 1 at any node, we conclude the tree is not balanced. To avoid multiple traversals for height calculation, we use a helper function that computes the height and checks the balance simultaneously.

Complexity Analysis:
- Time Complexity: O(N), where N is the number of nodes in the binary tree. Each node is visited once to compute its height and check balance.
- Space Complexity: O(H), where H is the height of the binary tree. This space is used by the recursion stack. In the worst case (the tree is completely unbalanced), the space complexity can be O(N).

Solution:
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkHeight(node):
            # Base case: An empty tree is balanced and has height -1
            if not node:
                return 0

            # Check heights of left and right subtrees
            leftHeight = checkHeight(node.left)
            rightHeight = checkHeight(node.right)

            # If left or right is unbalanced, propagate the failure upwards
            if (
                leftHeight == -1
                or rightHeight == -1
                or abs(leftHeight - rightHeight) > 1
            ):
                return -1

            # Return the height of the current node
            return max(leftHeight, rightHeight) + 1

        return checkHeight(root) != -1


# Example usage
if __name__ == "__main__":
    # Tree construction for example
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    sol = Solution()
    print(sol.isBalanced(root))  # Output: True
