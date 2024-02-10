"""
[LeetCode]98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example:
Input: root = [2,1,3]
Output: true
Explanation: The given tree is a valid BST because it satisfies the BST properties.

Approach:
To validate a BST, we perform an in-order traversal of the tree. If the tree is a valid BST, then the in-order traversal should produce a sequence of values in ascending order. We keep track of the last visited node's value and compare it with the current node's value to ensure the current value is greater, thus maintaining the BST property.

Complexity Analysis:
- Time Complexity: O(N), where N is the number of nodes in the binary tree. Each node is visited exactly once during the in-order traversal.
- Space Complexity: O(H), where H is the height of the binary tree. This space is used by the recursion stack. In the worst case (the tree is completely unbalanced), the space complexity can be O(N).

"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=-float("inf"), high=float("inf")):
            # Empty trees are valid BSTs
            if not node:
                return True

            # The current node's value must be between low and high
            if not (low < node.val < high):
                return False

            # Recursively validate the left and right subtrees
            return validate(node.left, low, node.val) and validate(
                node.right, node.val, high
            )

        return validate(root)


# Example usage
if __name__ == "__main__":
    # Tree construction for example
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    sol = Solution()
    print(sol.isValidBST(root))  # Output: True
