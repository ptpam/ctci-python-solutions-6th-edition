"""
[LeetCode]74. Search a 2D Matrix

Problem Statement:
Given an m x n matrix where each row is sorted in non-decreasing order and the first integer of each row is greater than the last integer of the previous row, determine if a target value is present in the matrix. This must be achieved in O(log(m*n)) time complexity.

Example:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: True

Solution Overview:
The matrix can be thought of as a flattened sorted list where the element at position 'i' in the list is present at matrix[i//n][i%n] in the matrix (n is the number of columns). We can apply binary search on this 'flattened' list to achieve O(log(m*n)) time complexity.

Solution Steps:
1. Perform a binary search to find the correct row where the target might be located. This is done by comparing the target with the first and last elements of a row.
2. Once the row is identified, perform a binary search on that row to find the target element.

Complexity Analysis:
- Time Complexity: O(log(m*n)), as binary search is performed twice: once for selecting the row and once for the element in the row.
- Space Complexity: O(1), as the solution uses constant extra space.

Solution Implementation:
"""


def searchMatrix(matrix, target):
    ROWS, COLS = len(matrix), len(matrix[0])

    # Binary search to find the correct row
    top, bot = 0, ROWS - 1
    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break

    if top > bot:
        return False  # Target is not present in any row

    # Binary search within the identified row
    row = (top + bot) // 2
    l, r = 0, COLS - 1
    while l <= r:
        m = (l + r) // 2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True  # Target found

    return False  # Target is not found


# Example of usage
if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    print(f"Is target {target} in matrix? {searchMatrix(matrix, target)}")

"""
This implementation demonstrates an efficient way to search for a target value in a 2D matrix by leveraging binary search, ensuring optimal time complexity as required.
"""
