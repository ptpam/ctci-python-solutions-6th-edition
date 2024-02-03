"""
Problem:
    Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

Approach:
    1. Use the first row and first column as markers for rows and columns to be set to 0.
    2. Traverse the matrix to mark the zero rows and columns.
    3. Nullify rows and columns based on the markers.
    4. Special handling for the first row and first column.

Complexity:
    Time: O(MxN), where M is the number of rows and N is the number of columns.
    Space: O(1), as we use the matrix itself for storage.
"""


def set_zeros(matrix):
    """
    Sets entire row and column to 0 if an element in an MxN matrix is 0.

    Args:
    matrix (List[List[int]]): The MxN matrix to modify.

    Returns:
    None: Modifies the matrix in place.
    """
    row_has_zero = False
    col_has_zero = False

    # Check if first row or column has a zero
    for j in range(len(matrix[0])):
        if matrix[0][j] == 0:
            row_has_zero = True
            break

    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            col_has_zero = True
            break

    # Mark rows and columns that need to be nullified
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Nullify marked rows and columns
    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            nullify_row(matrix, i)

    for j in range(1, len(matrix[0])):
        if matrix[0][j] == 0:
            nullify_col(matrix, j)

    # Nullify first row and column if necessary
    if row_has_zero:
        nullify_row(matrix, 0)

    if col_has_zero:
        nullify_col(matrix, 0)


def nullify_row(matrix, row):
    for j in range(len(matrix[0])):
        matrix[row][j] = 0


def nullify_col(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0


# Sample usage
matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
set_zeros(matrix)
print(matrix)  # Modified matrix with zeros
