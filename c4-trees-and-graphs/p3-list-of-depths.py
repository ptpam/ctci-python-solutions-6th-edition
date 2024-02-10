"""
[LeetCode]102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

This problem involves traversing a binary tree in a breadth-first manner, where we visit all nodes at the current depth before moving on to the nodes at the next depth.

Approach:
To achieve level order traversal, we use a queue to keep track of nodes and their levels while traversing the tree. We start with the root node and process nodes level by level, adding their children to the queue. This way, nodes are processed in order of their level, and we collect their values in a list corresponding to each level.

Complexity Analysis:
- Time Complexity: O(N), where N is the number of nodes in the binary tree. Each node is processed exactly once.
- Space Complexity: O(N) to hold the output and the queue, which in the worst case may contain all nodes in one level of the binary tree.

"""

from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([(root, 0)])  # Node with its level

        while queue:
            node, level = queue.popleft()
            if node:
                if len(result) == level:
                    result.append([])
                result[level].append(node.val)
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))

        return result


# Example usage
if __name__ == "__main__":
    # Tree construction for example
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    sol = Solution()
    print(sol.levelOrder(root))  # Output: [[3], [9, 20], [15, 7]]
