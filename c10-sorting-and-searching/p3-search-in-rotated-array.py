"""
Search in Rotated Array

Problem Statement:
Given a sorted array of n integers that has been rotated an unknown number of times, write code to find an element in the array. 
The array was originally sorted in increasing order.

Example:
Input: find 5 in {15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
Output: 8 (the index of 5 in the array)

Solution Overview:
The key is to identify which half of the array is normally ordered, and then determine if the target value lies within that normally ordered half. 
If it does, search that half; otherwise, search the other half. Handle the case where the left and middle elements are identical separately, as it may require searching both halves.

Complexity Analysis:
- Time Complexity: O(log n) in the best case (when all elements are unique). With many duplicates, the worst-case complexity becomes O(n).
- Space Complexity: O(1), as the solution uses constant space.

Solution Implementation:
"""


def search(a, left, right, x):
    if right < left:
        return -1

    mid = (left + right) // 2
    if x == a[mid]:  # Found element
        return mid

    # Determine which half is normally ordered
    if a[left] < a[mid]:  # Left is normally ordered
        if a[left] <= x < a[mid]:
            return search(a, left, mid - 1, x)  # Search left
        else:
            return search(a, mid + 1, right, x)  # Search right
    elif a[mid] < a[left]:  # Right is normally ordered
        if a[mid] < x <= a[right]:
            return search(a, mid + 1, right, x)  # Search right
        else:
            return search(a, left, mid - 1, x)  # Search left
    elif a[left] == a[mid]:  # Left or right half is all repeats
        if a[mid] != a[right]:  # If right is different, search it
            return search(a, mid + 1, right, x)  # search right
        else:  # Else, we have to search both halves
            result = search(a, left, mid - 1, x)  # Search left
            if result == -1:
                return search(a, mid + 1, right, x)  # Search right
            else:
                return result
    return -1


# Example of usage:
if __name__ == "__main__":
    array = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    target = 5
    print(f"Index of {target} in the array: {search(array, 0, len(array) - 1, target)}")

"""
This implementation provides an efficient way to find an element in a rotated sorted array by exploiting the property that one half of the array must be normally ordered. It carefully handles the case of duplicates, which could potentially require searching both halves of the array.
"""
