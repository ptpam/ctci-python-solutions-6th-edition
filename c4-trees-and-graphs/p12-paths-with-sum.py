"""
[LeetCode]437. Path Sum III

Problem Statement:
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum. The path does not need to start or end at the root or a leaf but must go downwards.

Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

Approach:
Use a recursive function to traverse the tree. For each node, explore all downward paths and count those whose sum equals targetSum. This involves two recursive calls:
1. One call continues the current path.
2. Another call starts a new path from the current node.

Complexity Analysis:
- Time Complexity: O(N^2) in the worst case for an unbalanced tree, where N is the number of nodes. Each node is visited, and for each node, we explore all paths downwards.
- Space Complexity: O(N) for the recursion stack in the worst case.

"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum_1(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        # Helper function to count paths with the given sum starting from the given node
        def countPaths(node, currentSum):
            if not node:
                return 0

            currentSum += node.val
            pathCount = 1 if currentSum == targetSum else 0

            # Count paths including the left and right child nodes
            pathCount += countPaths(node.left, currentSum)
            pathCount += countPaths(node.right, currentSum)

            return pathCount

        # Count paths from the current node, then try starting from the left and right child nodes
        pathsFromRoot = countPaths(root, 0)
        pathsFromLeft = self.pathSum_1(root.left, targetSum)
        pathsFromRight = self.pathSum_1(root.right, targetSum)

        return pathsFromRoot + pathsFromLeft + pathsFromRight

    def pathSum_2(self, root: Optional[TreeNode], targetSum: int) -> int:

        def incrementHashTable(hashTable, key, delta):
            hashTable[key] = hashTable.get(key, 0) + delta
            if hashTable[key] == 0:
                del hashTable[key]  # Clean up to save space

        def countPathsWithSum(node, targetSum, runningSum, pathCount):
            if not node:
                return 0

            runningSum += node.val
            sum = runningSum - targetSum
            totalPaths = pathCount.get(sum, 0)

            if runningSum == targetSum:
                totalPaths += 1  # Add paths starting from the root

            incrementHashTable(pathCount, runningSum, 1)  # Track current sum
            totalPaths += countPathsWithSum(node.left, targetSum, runningSum, pathCount)
            totalPaths += countPathsWithSum(
                node.right, targetSum, runningSum, pathCount
            )
            incrementHashTable(
                pathCount, runningSum, -1
            )  # Remove current sum before going up the stack

            return totalPaths

        return countPathsWithSum(root, targetSum, 0, {})


# Example usage
if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(
        5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))
    )
    root.right = TreeNode(-3, None, TreeNode(11))
    targetSum = 8
    sol = Solution()
    print(sol.pathSum_1(root, targetSum))  # Output: 3
    print(sol.pathSum_2(root, targetSum))  # Output: 3
