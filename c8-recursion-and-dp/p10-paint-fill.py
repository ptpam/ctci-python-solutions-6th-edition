"""
[LeetCode]733. Flood Fill

Problem Statement:
An image is represented by an m x n integer grid where image[i][j] represents the pixel value of the image. Given three integers sr, sc, and color, perform a flood fill starting from the pixel image[sr][sc]. All pixels connected 4-directionally to the starting pixel with the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels with the same color, should be colored with the new color. Return the modified image after performing the flood fill.

Example:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]

Approach:
- Utilize depth-first search (DFS) to explore all 4-directionally connected pixels of the same color.
- Avoid revisiting pixels by checking if the current pixel's color is already the new color.
- Recursively apply the flood fill to all eligible neighboring pixels.

Complexity Analysis:
- Time Complexity: O(m*n), where m is the number of rows and n is the number of columns in the image. In the worst case, we might need to visit every pixel once.
- Space Complexity: O(m*n) in the worst case for the call stack due to recursion, which occurs in a scenario where all pixels need to be repainted, and the recursion depth equals the number of pixels.

Solution Implementation:
"""

from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        originalColor = image[sr][sc]
        if (
            originalColor == color
        ):  # Base case: If the color is the same, no action is needed
            return image

        def dfs(r, c):
            if (
                r < 0
                or r >= len(image)
                or c < 0
                or c >= len(image[0])
                or image[r][c] != originalColor
            ):
                return
            image[r][c] = color
            # Recursive DFS for 4-directionally connected pixels
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image


# Example usage
if __name__ == "__main__":
    solution = Solution()
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr, sc, color = 1, 1, 2
    print("Modified image after flood fill:", solution.floodFill(image, sr, sc, color))
