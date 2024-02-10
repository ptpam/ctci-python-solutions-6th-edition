"""
[LeetCode]572. Subtree of Another Tree

Problem Statement:
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values as subRoot and false otherwise. A subtree of a binary tree tree is a tree consisting of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Explanation: There is a subtree of root with the same structure and node values as subRoot.

Approach:
The approach is to traverse the tree 'root' and compare each node with the root of 'subRoot' using a helper function. The helper function will check if two trees are identical. This involves checking if the current nodes of both trees are non-null and have the same value, and then recursively checking the left and right subtrees.

1. Traverse the tree 'root' (using pre-order, in-order, or post-order traversal).
2. For each node in 'root', use the helper function to check if the subtree rooted at the current node is identical to 'subRoot'.
3. If the helper function returns true at any point, return true.
4. If the traversal is completed without finding an identical subtree, return false.

Complexity Analysis:
- Time Complexity: O(n * m), where n is the number of nodes in 'root' and m is the number of nodes in 'subRoot'. In the worst case, we might need to check each node in 'root' against 'subRoot'.
- Space Complexity: O(h), where h is the height of the tree 'root'. This space is required for the recursion stack. In the worst case (a skewed tree), the space complexity can be O(n).

Solution:
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        return (
            s.val == t.val
            and self.isSameTree(s.left, t.left)
            and self.isSameTree(s.right, t.right)
        )


# Example usage
if __name__ == "__main__":
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    subRoot = TreeNode(4, TreeNode(1), TreeNode(2))

    sol = Solution()
    print(sol.isSubtree(root, subRoot))  # Output: True
