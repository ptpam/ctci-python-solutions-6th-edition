"""
Problem:
    Given two strings, write a function to check if they are one edit (or zero edits) away. An edit is insert, remove, or replace a character.

Approach:
    1. If strings differ in length by more than 1, return False.
    2. Check if they are one replacement away (same length).
    3. Check if they are one insertion or removal away (length differs by one).
    4. Merge insertion and removal into one step as they are inverse operations.

Complexity:
    Time: O(n), where n is the length of the shorter string.
    Space: O(1).
"""


def one_edit_away(first, second):
    """
    Checks if two strings are one edit away from each other.

    Args:
    first, second (str): Strings to be compared.

    Returns:
    bool: True if they are one edit away, False otherwise.
    """
    if abs(len(first) - len(second)) > 1:
        return False

    # Get shorter and longer string
    s1 = first if len(first) < len(second) else second
    s2 = second if len(first) < len(second) else first

    index1, index2 = 0, 0
    found_difference = False

    while index2 < len(s2) and index1 < len(s1):
        if s1[index1] != s2[index2]:
            if found_difference:
                return False
            found_difference = True

            if len(s1) == len(s2):
                index1 += 1  # On replace, move shorter pointer
        else:
            index1 += 1  # If matching, move shorter pointer

        index2 += 1  # Always move pointer for longer string

    return True


# Sample usage
print(one_edit_away("pale", "ple"))  # True
print(one_edit_away("pales", "pale"))  # True
print(one_edit_away("pale", "bale"))  # True
print(one_edit_away("pale", "bake"))  # False
