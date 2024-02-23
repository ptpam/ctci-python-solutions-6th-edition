"""
Sorted Merge

Problem Statement:
You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. 
Write a method to merge B into A in sorted order.

Solution Overview:
The solution involves merging the two arrays from the back to the front, by comparing the last elements of A and B and placing the larger one in the last position of the buffer in A. 
This process is repeated until all elements in B are merged into A, ensuring the merged array remains sorted.

Solution Details:
- Start from the end of A and B, compare their elements, and copy the larger one to the end of the buffer in A.
- Decrement the index of the array from which the element was taken, and also decrement the index of the current position in the buffer.
- Repeat this process until all elements from B are merged into A.

Complexity Analysis:
- Time Complexity: O(N + M), where N is the number of elements in A, and M is the number of elements in B. Each element in A and B is looked at once.
- Space Complexity: O(1), no additional space is required as the merged array is stored in the existing buffer in A.

Solution Implementation:
"""


def merge(A, B, lastA, lastB):
    """
    Merges array B into array A in sorted order.
    Args:
    A: Sorted array with a buffer at the end to hold B
    B: Sorted array to merge into A
    lastA: Number of actual elements in array A
    lastB: Number of elements in array B
    """
    indexA = lastA - 1  # Index of last element in array A
    indexB = lastB - 1  # Index of last element in array B
    indexMerged = lastB + lastA - 1  # End of merged array

    # Merge A and B, starting from the last element in each
    while indexB >= 0:
        if indexA >= 0 and A[indexA] > B[indexB]:
            A[indexMerged] = A[indexA]
            indexA -= 1
        else:
            A[indexMerged] = B[indexB]
            indexB -= 1
        indexMerged -= 1


# Example of usage:
if __name__ == "__main__":
    A = [2, 4, 6, 8, None, None, None]
    B = [1, 3, 5]
    merge(A, B, 4, 3)
    print("Merged A:", A)

"""
The merge function efficiently combines two sorted arrays into a single sorted array in-place, using the buffer space provided at the end of array A. This solution maintains the sorted order of elements and leverages the given buffer space for an optimal in-place merging process.
"""
