"""
Problem:
    Write a method to replace all spaces in a string with '%20'. Assume the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.

Approach:
    1. Use a two-scan approach.
    2. First scan: Count the number of spaces to determine the adjusted length of the string.
    3. Second scan (reverse order): Replace spaces with '%20' and shift non-space characters.

Complexity:
    Time: O(n), where 'n' is the true length of the string.
    Space: O(1), in-place modification.
"""


def urlify(string, true_length):
    """
    Replace spaces in a string with '%20'.

    Args:
    string (str): The string to be modified.
    true_length (int): The "true" length of the string.

    Returns:
    str: The modified string with spaces replaced by '%20'.
    """
    # Convert string to a list to allow in-place modification
    characters = list(string)
    space_count = characters[:true_length].count(" ")
    new_index = true_length + space_count * 2

    for i in range(true_length - 1, -1, -1):
        if characters[i] == " ":
            characters[new_index - 3 : new_index] = "%20"
            new_index -= 3
        else:
            characters[new_index - 1] = characters[i]
            new_index -= 1

    return "".join(characters[: new_index + space_count * 2])


# Sample usage
print(urlify("Mr John Smith    ", 13))  # "Mr%20John%20Smith"
