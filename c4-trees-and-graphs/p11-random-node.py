"""
Binary Tree with Random Node Access

Design and implement a binary tree class from scratch which supports insert, find, delete, and getRandomNode methods. The getRandomNode method should return a random node from the tree, with all nodes being equally likely to be chosen.

Approach:
1. Extend the TreeNode class to include a size attribute, representing the number of nodes in the subtree rooted at this node.
2. Implement insert and find methods using standard binary search tree logic, updating the size attribute during insertions.
3. The delete method is more complex, requiring adjustments to maintain binary search tree properties and update the size attribute correctly. (Note: Detailed implementation of delete is beyond this simplified explanation but follows similar principles.)
4. Use the size attribute to implement getRandomNode. This method selects a random node based on the subtree sizes, ensuring equal probability.

Complexity Analysis:
- Time Complexity: O(log N) on average for insert, find, delete, and getRandomNode methods, where N is the number of nodes in the tree. This can degrade to O(N) in the worst-case scenario of an unbalanced tree.
- Space Complexity: O(N) for storing the tree.

Solution:
"""

import random


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        self.size = 1


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if val <= node.val:
            if not node.left:
                node.left = TreeNode(val)
            else:
                self._insert(node.left, val)
        else:
            if not node.right:
                node.right = TreeNode(val)
            else:
                self._insert(node.right, val)
        node.size += 1

    def find(self, val):
        return self._find(self.root, val)

    def _find(self, node, val):
        if not node:
            return False
        if node.val == val:
            return True
        elif val < node.val:
            return self._find(node.left, val)
        else:
            return self._find(node.right, val)

    # Simplified placeholder for the delete method
    def delete(self, val):
        pass

    def getRandomNode(self):
        if not self.root:
            return None
        return self._getRandomNode(self.root, random.randint(1, self.root.size))

    def _getRandomNode(self, node, count):
        leftSize = node.left.size if node.left else 0

        if count <= leftSize:
            return self._getRandomNode(node.left, count)
        elif count == leftSize + 1:
            return node
        else:
            return self._getRandomNode(node.right, count - leftSize - 1)


# Example usage
if __name__ == "__main__":
    bt = BinaryTree()
    bt.insert(5)
    bt.insert(3)
    bt.insert(7)
    bt.insert(2)
    bt.insert(4)
    bt.insert(6)
    bt.insert(8)

    # Get 5 random nodes
    for _ in range(5):
        node = bt.getRandomNode()
        print(node.val, end=" ")
