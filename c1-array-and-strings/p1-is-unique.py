"""
Problem:
    Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

Approach:
    1. Check string length against character set length. If string length exceeds character set (128 for ASCII), it has duplicates.
    2. Use a boolean array to track occurrences of each character. On encountering a repeated character, return False.
    3. Optimize space usage using a bit vector for lower case alphabets.
    4. Alternate solutions without additional data structures: brute force (O(n^2)) and sorting (O(n log n)).

Complexity:
    Time: O(n) or O(min(c, n)), where 'n' is string length and 'c' is character set size.
    Space: O(1), considering fixed-size character set; otherwise, O(c).
"""


def is_unique_chars(string):
    """
    Checks if a string has all unique characters.

    Args:
    string (str): The string to check.

    Returns:
    bool: True if all characters are unique, False otherwise.
    """
    if len(string) > 128:
        return False

    char_set = [False] * 128
    for char in string:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True
    return True


def is_unique_chars_bit_vector(string):
    """
    Checks if a string has all unique characters using a bit vector.
    Assumes only lowercase alphabets.

    Args:
    string (str): The string to check.

    Returns:
    bool: True if all characters are unique, False otherwise.
    """
    checker = 0
    for char in string:
        val = ord(char) - ord("a")
        if (checker & (1 << val)) > 0:
            return False
        checker |= 1 << val
    return True


# Sample usage
print(is_unique_chars("abcdef"))  # True
print(is_unique_chars("hello"))  # False
print(is_unique_chars_bit_vector("abcde"))  # True
print(is_unique_chars_bit_vector("apple"))  # False
