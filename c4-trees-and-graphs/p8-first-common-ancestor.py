"""
[LeetCode]236. Lowest Common Ancestor of a Binary Tree

Problem Statement:
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. 
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Approach:
The approach is to recursively traverse the binary tree and search for the nodes p and q. If either p or q is found (i.e., root matches either p or q), return the current node (root) to its parent. The LCA is found where both subtrees from a node have one of the nodes p or q, meaning this node is the lowest common ancestor.

1. Start from the root and traverse the tree.
2. If the current node is NULL, return NULL.
3. If the current node is equal to either p or q, return the current node.
4. Recur for the left and right children of the current node.
5. If both steps above return a non-NULL value, then one node is found in one subtree and the other node is found in the other subtree. So, this node is the LCA.
6. If only one subtree returns a non-NULL value, then both nodes are located in that subtree.
7. If both sides return NULL, then neither node is present in the subtree.

Complexity Analysis:
- Time Complexity: O(N), where N is the number of nodes in the binary tree. In the worst case, we might visit all the nodes.
- Space Complexity: O(H), where H is the height of the tree. This space is required for the recursion stack. In the worst case, the space complexity can be O(N).

Solution:
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right are non-null, this is the LCA
        if left and right:
            return root

        # Either one of left or right is the LCA
        return left if left else right


# Example usage
if __name__ == "__main__":
    # Construct binary tree for example
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    p = root.left  # Node 5
    q = root.right  # Node 1

    sol = Solution()
    lca = sol.lowestCommonAncestor(root, p, q)
    print(lca.val)  # Output: 3
