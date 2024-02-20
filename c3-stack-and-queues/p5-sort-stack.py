"""
Sort Stack

Problem Statement:
Write a program to sort a stack such that the smallest items are on the top. 
You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array). 
The stack supports the following operations: push, pop, peek, and isEmpty.

Solution Overview:
The task is to sort a stack with the smallest items on top using only one additional stack for temporary storage. 
The approach involves repeatedly removing elements from the input stack (s), comparing each element with the top of the temporary (sorted) stack (r), and ensuring elements in (r) are always in sorted order. 
If the current element (tmp) is smaller than the top of (r), we temporarily move elements from (r) back to (s) until we find the correct position for (tmp).

Solution Approach:
1. Use an additional stack (r) to store elements in sorted order.
2. Repeatedly pop elements from the original stack (s), and insert them into the correct position in (r) to maintain sorted order.
3. After processing all elements, transfer them back from (r) to (s) to have the smallest items on top in the original stack.

Complexity Analysis:
- Time Complexity: O(N^2), where N is the number of elements in the stack. Each element, in the worst case, may need to be compared with every element already in the sorted stack.
- Space Complexity: O(N) for the additional stack used for sorting.

Solution Implementation:
"""


class Stack:
    def __init__(self):
        self.container = []

    def push(self, item):
        self.container.append(item)

    def pop(self):
        if not self.is_empty():
            return self.container.pop()

    def peek(self):
        if not self.is_empty():
            return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


def sort_stack(original_stack):
    sorted_stack = Stack()
    while not original_stack.is_empty():
        # Pop each element from the original stack
        tmp = original_stack.pop()
        # Move elements from sorted_stack back to original_stack if they are greater than tmp
        while not sorted_stack.is_empty() and sorted_stack.peek() > tmp:
            original_stack.push(sorted_stack.pop())
        # Push tmp in its correct position in sorted_stack
        sorted_stack.push(tmp)

    # Transfer elements back to original_stack so that the smallest items are on top
    while not sorted_stack.is_empty():
        original_stack.push(sorted_stack.pop())


# Example of usage:
if __name__ == "__main__":
    s = Stack()
    s.push(3)
    s.push(1)
    s.push(4)
    s.push(2)

    sort_stack(s)

    # Printing sorted stack
    while not s.is_empty():
        print(s.pop())

"""
Note: The sort_stack function modifies the original stack to have the smallest items on the top, using only one additional stack for temporary storage. 
This efficient approach ensures that the stack is sorted as required, with all operations conforming to the stack data structure's standard operations.
"""
