"""
Magic Index Problem

A Magic Index in an array A[0...n-1] is defined as an index such that A[i] = i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in the array A.

Follow-up: How would you solve the problem if the values are not distinct?

Solution:
The problem is a variation of the binary search due to the array's sorted nature. For arrays with distinct elements, a modified binary search can efficiently find the magic index. However, for arrays with non-distinct elements, the approach needs to be adapted to account for the possibility of multiple valid paths due to repeated elements.

Complexity Analysis:
- Time Complexity:
For distinct elements: O(log n), where n is the number of elements in the array.
For non-distinct elements: Potentially O(n), in the worst case, due to the need to explore parts of both halves of the array.
- Space Complexity: O(log n) for both cases due to the recursion stack depth in a binary search.

1. For Distinct Elements:
"""


def magicFastDistinct(array):
    def helper(array, start, end):
        if end < start:
            return -1
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            return helper(array, start, mid - 1)
        else:
            return helper(array, mid + 1, end)

    return helper(array, 0, len(array) - 1)


"""
2. For Non-Distinct Elements:
The search space is reduced based on the comparison of midIndex and midValue, considering the potential for repeated elements.
"""


def magicFastNonDistinct(array):
    def helper(array, start, end):
        if end < start:
            return -1
        midIndex = (start + end) // 2
        midValue = array[midIndex]
        if midValue == midIndex:
            return midIndex
        # Search left
        leftIndex = min(midIndex - 1, midValue)
        left = helper(array, start, leftIndex)
        if left >= 0:
            return left
        # Search right
        rightIndex = max(midIndex + 1, midValue)
        return helper(array, rightIndex, end)

    return helper(array, 0, len(array) - 1)


# Example usage
if __name__ == "__main__":
    # For distinct elements
    distinct_array = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
    print("Magic Index (Distinct):", magicFastDistinct(distinct_array))

    # For non-distinct elements
    non_distinct_array = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
    print("Magic Index (Non-Distinct):", magicFastNonDistinct(non_distinct_array))
