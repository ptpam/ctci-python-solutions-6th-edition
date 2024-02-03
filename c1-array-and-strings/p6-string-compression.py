"""
Problem:
    Implement a method to perform basic string compression using the counts of repeated characters. If the compressed string would not become smaller than the original string, return the original string.

Approach:
    1. Iterate through the string, count consecutive characters.
    2. If the current character is different from the next, append it and its count to the result.
    3. Optimize by checking the final length in advance and using a StringBuilder-like structure.

Complexity:
    Time: O(n), where n is the length of the string.
    Space: O(n), for the new string.
"""


def compress_string(string):
    """
    Compresses a string by replacing sequences of repeated characters with the character followed by the count.

    Args:
    string (str): The string to compress.

    Returns:
    str: The compressed string or original string if compression does not reduce the size.
    """
    final_length = count_compression(string)
    if final_length >= len(string):
        return string

    compressed = []
    count_consecutive = 0

    for i in range(len(string)):
        count_consecutive += 1

        if i + 1 >= len(string) or string[i] != string[i + 1]:
            compressed.append(string[i])
            compressed.append(str(count_consecutive))
            count_consecutive = 0

    return "".join(compressed)


def count_compression(string):
    """
    Counts the length of the string after compression.

    Args:
    string (str): The string to be compressed.

    Returns:
    int: The length of the string after compression.
    """
    compressed_length = 0
    count_consecutive = 0

    for i in range(len(string)):
        count_consecutive += 1

        if i + 1 >= len(string) or string[i] != string[i + 1]:
            compressed_length += 1 + len(str(count_consecutive))
            count_consecutive = 0

    return compressed_length


# Sample usage
print(compress_string("aabcccccaaa"))  # "a2b1c5a3"
print(compress_string("abcdef"))  # "abcdef"
