"""
Sparse Search

Problem Statement:
Given a sorted array of strings that is interspersed with empty strings, write a method to find the location of a given string.

Example:
Input: "ball", ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
Output: 4

Solution Overview:
The approach is a modified binary search. 
The key modification is to adjust the mid-point to the closest non-empty string if the mid-point directly lands on an empty string, before proceeding with the standard binary search comparison.

Solution Details:
1. Perform a binary search, but adjust mid if strings[mid] is an empty string by moving mid to the nearest non-empty string.
2. Once a non-empty mid is found, proceed with a standard binary search step (compare strings[mid] with the target string and decide the direction of search).

Complexity Analysis:
- Time Complexity: O(n) in the worst case, where n is the number of elements in the array. This happens when we need to linearly search for the nearest non-empty string for comparison.
- Space Complexity: O(1), as the solution uses constant extra space.

Solution Implementation:
"""


def sparse_search(strings, target_str):
    def search(strings, target_str, first, last):
        if first > last:
            return -1

        mid = (first + last) // 2

        # Adjust mid for empty string
        if strings[mid] == "":
            left, right = mid - 1, mid + 1
            while True:
                if left < first and right > last:
                    return -1
                elif right <= last and strings[right] != "":
                    mid = right
                    break
                elif left >= first and strings[left] != "":
                    mid = left
                    break
                right += 1
                left -= 1

        # Binary search comparison
        if strings[mid] == target_str:
            return mid
        elif strings[mid] < target_str:
            return search(strings, target_str, mid + 1, last)
        else:
            return search(strings, target_str, first, mid - 1)

    if not strings or target_str == "":
        return -1
    return search(strings, target_str, 0, len(strings) - 1)


# Example of usage:
if __name__ == "__main__":
    strings = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    target_str = "ball"
    print(f"Index of '{target_str}' in the array: {sparse_search(strings, target_str)}")

"""
This implementation addresses the challenge posed by interspersed empty strings in a sorted array. By adjusting the binary search approach to account for these empty strings, we can efficiently locate the desired string while handling the sparse nature of the data structure.
"""
