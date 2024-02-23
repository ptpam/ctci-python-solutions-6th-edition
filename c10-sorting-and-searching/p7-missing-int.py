"""
Missing Int

Problem Statement:
Given an input file with four billion non-negative integers, provide an algorithm to generate an integer not contained in the file with 1 GB of memory available. For the follow-up, if only 10 MB of memory is available and all values are distinct with no more than one billion non-negative integers, adjust the algorithm accordingly.

Solution Overview:
With 1 GB of memory, we can create a bit vector with 4 billion bits to map all possible integers. Using this, we flag each integer we read from the file. The first unflagged position in the bit vector corresponds to a missing integer.

For the follow-up with 10 MB of memory:
1. Divide the integers into blocks.
2. Count the number of integers in each block in the first pass.
3. Use a bit vector to find a missing integer within the block that has missing integers.

Solution Implementation:
"""


def find_missing_integer(filename):
    # Assuming implementation details for reading the file and bit vector setup are abstracted
    number_of_ints = 2**32
    bit_vector = [0] * (number_of_ints // 8)

    # Process file and flag each integer
    with open(filename, "r") as file:
        for line in file:
            n = int(line.strip())
            bit_vector[n // 8] |= 1 << (n % 8)

    # Find the first 0 bit
    for i in range(len(bit_vector)):
        for j in range(8):
            if not (bit_vector[i] & (1 << j)):
                return i * 8 + j


def find_missing_integer_with_limited_memory(filename):
    range_size = 2**20  # Example range size for demonstration
    blocks = [0] * (2**31 // range_size)

    # First pass to count numbers in each block
    with open(filename, "r") as file:
        for line in file:
            n = int(line.strip())
            blocks[n // range_size] += 1

    # Find block with missing integer
    for block_index, count in enumerate(blocks):
        if count < range_size:
            # Second pass within the identified block
            bit_vector = [0] * (range_size // 8)
            start_range = block_index * range_size
            end_range = start_range + range_size

            with open(filename, "r") as file:
                for line in file:
                    n = int(line.strip())
                    if start_range <= n < end_range:
                        bit_vector[(n - start_range) // 8] |= 1 << (
                            (n - start_range) % 8
                        )

            # Find missing integer in the bit vector
            for i in range(len(bit_vector)):
                for j in range(8):
                    if not (bit_vector[i] & (1 << j)):
                        return start_range + i * 8 + j


# Example Usage
if __name__ == "__main__":
    filename = "input_numbers.txt"
    print(f"Missing integer (1GB memory): {find_missing_integer(filename)}")
    print(
        f"Missing integer (10MB memory): {find_missing_integer_with_limited_memory(filename)}"
    )
