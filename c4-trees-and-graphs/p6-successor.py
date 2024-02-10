"""
[Leetcode] 285. Inorder Successor in BST

Given a binary search tree (BST) and a node in it, find the in-order successor of that node in the BST. 
The successor of a node p is the node with the smallest key greater than p.val

Example:
Input: root = [5,3,6,2,4,null,null,1], p = 3
Output: 4
Explanation: In the in-order traversal of the given BST, the nodes are visited in the order: 1, 2, 3, 4, 5, 6. 
The successor of node 3 is node 4.

Approach:
To find the in-order successor of a given node, we can utilize the properties of a BST. 
If the node has a right child, then its successor is the leftmost node in its right subtree. 
If the node does not have a right child, we traverse from the root to the given node and keep track of the last node for which the given node would be in the left subtree, which will be the successor.

Complexity Analysis:
- Time Complexity: O(H), where H is the height of the tree. This is because we are making a single pass from the root to the leaf in the worst case.
- Space Complexity: O(1), as no additional space is needed apart from temporary variables.

Solution:
"""


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        # Initialize variable to store the inorder successor
        successor = None

        # Traverse the tree starting with the root
        while root:
            # If current node's value is greater than 'p's value,
            # tentative successor is found (potentially there could be a closer one).
            if root.val > p.val:
                successor = root
                # Move to the left subtree to find the closest ancestor
                root = root.left
            else:
                # If current node's value is less than or equal to 'p's value,
                # the successor must be in the right subtree.
                root = root.right

        # Return the successor node
        return successor


# Example usage
if __name__ == "__main__":
    # Tree construction for example
    root = TreeNode(5)
    root.left = TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4))
    root.right = TreeNode(6)
    p = root.left  # Node with value 3

    sol = Solution()
    successor = sol.inorderSuccessor(root, p)
    print(successor.val if successor else None)  # Output: 4
