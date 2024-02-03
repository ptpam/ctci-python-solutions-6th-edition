"""
Problem:
    Given a string, write a function to check if it is a permutation of a palindrome.

Approach:
    1. A string that is a permutation of a palindrome has at most one character with an odd count.
    2. Solution #1: Use a hash table to count occurrences of each character and then ensure no more than one character has an odd count.
    3. Solution #2: Incremental check of odd counts during the hash table creation.
    4. Solution #3: Use a bit vector to represent the odd/even status of character counts.

Complexity:
    Time: O(N) for each solution, where N is the length of the string.
    Space: O(1) for each solution, considering fixed-size character set.
"""


def is_permutation_of_palindrome(phrase):
    """
    Checks if the string is a permutation of a palindrome using character count.

    Args:
    phrase (str): The string to check.

    Returns:
    bool: True if it's a permutation of a palindrome, False otherwise.
    """
    table = [0] * 128  # Assuming ASCII character set
    count_odd = 0
    for char in phrase:
        x = ord(char)
        if x >= 0:
            table[x] += 1
            if table[x] % 2 == 1:
                count_odd += 1
            else:
                count_odd -= 1

    return count_odd <= 1


def create_bit_vector(phrase):
    """
    Creates a bit vector for the string. Each bit represents the odd/even status of a character's count.

    Args:
    phrase (str): The string to create a bit vector for.

    Returns:
    int: The bit vector representing the string.
    """
    bit_vector = 0
    for char in phrase:
        x = ord(char)
        bit_vector ^= 1 << x

    return bit_vector


def check_exactly_one_bit_set(bit_vector):
    """
    Checks if exactly one bit is set in the bit vector.

    Args:
    bit_vector (int): The bit vector to check.

    Returns:
    bool: True if exactly one bit is set, False otherwise.
    """
    return bit_vector & (bit_vector - 1) == 0


def is_permutation_of_palindrome_bit_vector(phrase):
    """
    Checks if the string is a permutation of a palindrome using a bit vector.

    Args:
    phrase (str): The string to check.

    Returns:
    bool: True if it's a permutation of a palindrome, False otherwise.
    """
    bit_vector = create_bit_vector(phrase)
    return bit_vector == 0 or check_exactly_one_bit_set(bit_vector)


# Sample usage
print(is_permutation_of_palindrome("tactcoapapa"))  # True
print(is_permutation_of_palindrome_bit_vector("tactcoapapa"))  # True
