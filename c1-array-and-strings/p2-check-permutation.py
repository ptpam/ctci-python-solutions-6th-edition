"""
Problem:
    Given two strings, write a method to decide if one is a permutation of the other. The comparison is case sensitive and whitespace is significant.

Approach:
    1. Confirm character set (ASCII assumed here) and case sensitivity.
    2. Check if strings are of equal length. If not, they cannot be permutations.
    3. Solution 1: Sort both strings and compare.
    4. Solution 2: Check if both strings have identical character counts.

Complexity:
    Solution 1: Time - O(n log n), Space - O(1)
    Solution 2: Time - O(n), Space - O(1) (considering fixed-size character set)
"""


def are_permutations_sort(s, t):
    """
    Checks if two strings are permutations of each other by sorting.

    Args:
    s, t (str): Strings to be compared.

    Returns:
    bool: True if they are permutations of each other, False otherwise.
    """
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


def are_permutations_char_count(s, t):
    """
    Checks if two strings are permutations of each other by character count.

    Args:
    s, t (str): Strings to be compared.

    Returns:
    bool: True if they are permutations of each other, False otherwise.
    """
    if len(s) != len(t):
        return False

    letters = [0] * 128  # Assuming ASCII character set
    for char in s:
        letters[ord(char)] += 1

    for char in t:
        letters[ord(char)] -= 1
        if letters[ord(char)] < 0:
            return False

    return True


# Sample usage
print(are_permutations_sort("god", "dog"))  # True
print(are_permutations_sort("god ", "dog"))  # False
print(are_permutations_char_count("god", "dog"))  # True
print(are_permutations_char_count("god ", "dog"))  # False
