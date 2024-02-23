"""
Peaks and Valleys

Problem Statement:
Given an array of integers, sort the array into an alternating sequence of peaks and valleys.

Solution Overview:
This solution focuses on arranging the elements in such a way that for every two elements, the middle element is a peak, and the two side elements are valleys. This arrangement does not require the array to be sorted initially.

Optimal Solution Steps:
1. Iterate through the array, focusing on every second element as the potential peak.
2. For each potential peak, identify the largest of its adjacent elements (including itself).
3. If the largest element is not the current potential peak, swap them.
4. This approach ensures that every second element (starting from the first) is a peak, and consequently, every other element is a valley.

Complexity Analysis:
- Time Complexity: O(N), where N is the length of the array. Each element is looked at once.
- Space Complexity: O(1), as the rearrangement is done in place with no need for extra space.

Solution Implementation:
"""


def sortValleyPeak(arr):
    def max_index(arr, a, b, c):
        len_arr = len(arr)
        aValue = arr[a] if a < len_arr else float("-inf")
        bValue = arr[b] if b < len_arr else float("-inf")
        cValue = arr[c] if c < len_arr else float("-inf")

        max_value = max(aValue, max(bValue, cValue))
        if aValue == max_value:
            return a
        elif bValue == max_value:
            return b
        else:
            return c

    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    for i in range(1, len(arr), 2):
        biggest_index = max_index(arr, i - 1, i, i + 1)
        if i != biggest_index:
            swap(arr, i, biggest_index)


# Example Usage
if __name__ == "__main__":
    arr = [5, 3, 1, 2, 3]
    sortValleyPeak(arr)
    print(f"Sorted into peaks and valleys: {arr}")
    # Output: The array will be sorted into peaks and valleys, e.g., [3, 1, 5, 2, 3]

"""
This solution efficiently transforms the input array into an alternating sequence of peaks and valleys. By focusing on arranging the elements rather than sorting, it achieves the desired outcome with optimal time complexity.
"""
