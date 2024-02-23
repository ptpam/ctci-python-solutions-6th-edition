"""
Find Duplicates

Problem Statement:
Given an array with all numbers from 1 to N (N <= 32,000), print all duplicate elements in the array with only 4 kilobytes of memory available.

Solution Overview:
With 4 kilobytes of memory, we can manage a bit vector (bitset) to track the occurrence of each number in the array. 
Each bit in the bitset corresponds to a number, allowing us to flag numbers as we encounter them. 
If we encounter a number that is already flagged, it indicates a duplicate, which we then print.

Solution Details:
- Initialize a bit vector large enough to flag all numbers from 1 to N (32,000 bits are sufficient, fitting within the 4KB memory constraint).
- Iterate through the array, using the bit vector to flag each number.
- When a number is encountered that is already flagged, print it as a duplicate.

Complexity Analysis:
- Time Complexity: O(N), where N is the length of the array. Each element in the array is visited exactly once.
- Space Complexity: O(1), the bit vector uses a fixed amount of memory (4KB), independent of the input array size.

Solution Implementation:
"""


class BitSet:
    def __init__(self, size):
        self.bitset = [0] * ((size >> 5) + 1)  # divide by 32

    def set(self, num):
        self.bitset[num >> 5] |= 1 << (num & 31)  # num / 32, num % 32

    def get(self, num):
        return (self.bitset[num >> 5] & (1 << (num & 31))) != 0


def checkDuplicates(array):
    bs = BitSet(32000)
    for num in array:
        num0 = num - 1  # bitset starts at 0, numbers start at 1
        if bs.get(num0):
            print(num)
        else:
            bs.set(num0)


# Example of usage:
if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 5, 7, 8, 9, 10, 3, 11, 12, 13]
    print("Duplicate numbers are:")
    checkDuplicates(array)

"""
This implementation leverages a custom BitSet class to efficiently track and identify duplicate numbers within the given memory constraints. 
By mapping each number to a specific bit in the BitSet, we can quickly determine if a number has been seen before and print duplicates accordingly.
"""
