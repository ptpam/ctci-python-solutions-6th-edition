"""
Problem:
    Assume you have a method isSubstring which checks if one word is a substring of another.
    Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring.

Approach:
    1. Concatenate s1 with itself and check if s2 is a substring of the result.
    2. The idea is that if s2 is a rotation of s1, it will always be a substring of s1s1.

Complexity:
    Time: O(N), where N is the length of the string.
    Space: O(N), for the concatenated string.
"""


def is_rotation(s1, s2):
    """
    Checks if s2 is a rotation of s1.

    Args:
    s1, s2 (str): The strings to be checked.

    Returns:
    bool: True if s2 is a rotation of s1, False otherwise.
    """
    if len(s1) == len(s2) and len(s1) > 0:
        return is_substring(s1 + s1, s2)
    return False


def is_substring(s1, s2):
    """
    Checks if s2 is a substring of s1. This function is a placeholder for the actual 'isSubstring' method.

    Args:
    s1, s2 (str): The strings to be checked.

    Returns:
    bool: True if s2 is a substring of s1, False otherwise.
    """
    return s2 in s1


# Sample usage
print(is_rotation("waterbottle", "erbottlewat"))  # True
print(is_rotation("waterbottle", "erbottlewax"))  # False
