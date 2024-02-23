"""
Sorted Search, No Size

Problem Statement:
Given an array-like data structure Listy which lacks a size method but has an elementAt(i) method that returns the element at index i in O(1) time (returns -1 if i is out of bounds), 
find the index at which an element x occurs in a sorted list of positive integers.

Solution Overview:
The challenge lies in not knowing the length of the Listy. 
We can overcome this by first finding an upper bound for the length using exponential backoff, and then performing binary search within that range to find the target value.

Solution Details:
- Start with an index value of 1 and exponentially increase it until elementAt(index) returns -1 or a value greater than the target, finding an upper bound.
- Perform binary search between the found upper bound and half of this bound to locate the target value.

Complexity Analysis:
- Time Complexity: O(log n), where n is the position of the target value or the length of the Listy. Finding the length takes O(log n) and so does the binary search.
- Space Complexity: O(1), as the solution uses constant extra space.

Solution Implementation:
"""


class Listy:
    def __init__(self, arr):
        self.arr = arr

    def elementAt(self, i):
        if i < len(self.arr):
            return self.arr[i]
        return -1


def search(listy, value):
    # Finding the range for binary search
    index = 1
    while listy.elementAt(index) != -1 and listy.elementAt(index) < value:
        index *= 2
    return binarySearch(listy, value, index // 2, index)


def binarySearch(listy, value, low, high):
    while low <= high:
        mid = (low + high) // 2
        middle = listy.elementAt(mid)
        if middle == -1 or middle > value:
            high = mid - 1
        elif middle < value:
            low = mid + 1
        else:
            return mid
    return -1


# Example of usage:
if __name__ == "__main__":
    listy = Listy([1, 3, 5, 7, 9, 13, 15, 17, 19, 25, 30])
    target = 15
    print(f"Index of {target} in Listy: {search(listy, target)}")

"""
This implementation demonstrates how to conduct a sorted search in an array-like data structure without a size method, by first finding an upper bound and then applying binary search. The approach efficiently finds the target value's index with logarithmic time complexity.
"""
