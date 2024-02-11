"""
[LeetCode]62. Unique Paths

Problem Statement:
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]) and tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move down or right at any point in time. Given two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

Example:
Input: m = 3, n = 7
Output: 28

Approach:
The problem can be solved using dynamic programming. The number of ways to reach a particular cell is the sum of the ways to reach the cell directly above it and the cell to the left of it. This approach uses a single-dimensional array to store the number of ways to reach the cells in the current row, updating it for each row from top to bottom.

Complexity Analysis:
- Time Complexity: O(m*n), where m is the number of rows and n is the number of columns in the grid. Each cell's value is computed once.
- Space Complexity: O(n), where n is the number of columns. The solution maintains a single row of n elements.

Solution:
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(1, m):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]


# Example usage
if __name__ == "__main__":
    solution = Solution()
    m, n = 3, 7  # Example input
    print(f"Number of unique paths for a {m}x{n} grid: {solution.uniquePaths(m, n)}")
