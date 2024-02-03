"""
Problem:
    Given an image represented by an NxN matrix, where each pixel in the image is represented by an integer, write a method to rotate the image by 90 degrees. Can you do this in place?

Approach:
    1. Rotate the matrix in layers, starting from the outermost and working inwards.
    2. For each layer, perform a four-way swap of the edges.
    3. The swap is done index by index to avoid using additional memory.

Complexity:
    Time: O(N^2), as we need to touch each element once.
    Space: O(1), as the rotation is done in place.
"""


def rotate_matrix(matrix):
    """
    Rotates a given NxN matrix by 90 degrees clockwise in place.

    Args:
    matrix (List[List[int]]): The NxN matrix to be rotated.

    Returns:
    bool: True if rotation is successful, False otherwise.
    """
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False

    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first

            # Save the top
            top = matrix[first][i]

            # Left -> Top
            matrix[first][i] = matrix[last - offset][first]

            # Bottom -> Left
            matrix[last - offset][first] = matrix[last][last - offset]

            # Right -> Bottom
            matrix[last][last - offset] = matrix[i][last]

            # Top -> Right
            matrix[i][last] = top

    return True


# Sample usage
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate_matrix(matrix)
print(matrix)  # Rotated matrix
