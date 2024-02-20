"""
Three in One

Problem Statement:
Describe how you could use a single array to implement three stacks.

Approaches and Complexity Analysis:

1. Fixed Division Approach:
- Divide the array into three equal parts, each dedicated to one stack.
- This approach is simple and straightforward but might lead to space inefficiency if one stack requires more space while others have unused space.

Complexity Analysis:
- Time Complexity: O(1) for push, pop, and peek operations, since we're accessing and updating specific indices based on calculated offsets.
- Space Complexity: O(n) for the underlying array where n is the total size of the array divided equally among the three stacks.

2. Flexible Divisions Approach (Overview):
- Allow the stacks to dynamically resize based on the stored data, using a more complex strategy to manage and allocate the array space efficiently.
- This approach is more space-efficient but significantly increases the complexity of managing stack boundaries and shifting elements.

Complexity Analysis (Flexible Divisions):
- Time Complexity: Operations may take longer than O(1) due to the need for shifting elements when resizing and reallocating stack spaces.
- Space Complexity: Still O(n) for the underlying array, but utilizes the available space more efficiently across the stacks.

Fixed Division Implementation:
"""


class FixedMultiStack:
    def __init__(self, stack_size):
        self.num_stacks = 3
        self.stack_capacity = stack_size
        self.values = [0] * (stack_size * self.num_stacks)
        self.sizes = [0] * self.num_stacks

    def push(self, stack_num, value):
        if self.is_full(stack_num):
            raise Exception("Stack {} is full".format(stack_num))
        self.sizes[stack_num] += 1
        self.values[self.index_of_top(stack_num)] = value

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception("Stack {} is empty".format(stack_num))
        top_index = self.index_of_top(stack_num)
        value = self.values[top_index]
        self.values[top_index] = 0
        self.sizes[stack_num] -= 1
        return value

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception("Stack {} is empty".format(stack_num))
        return self.values[self.index_of_top(stack_num)]

    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0

    def is_full(self, stack_num):
        return self.sizes[stack_num] == self.stack_capacity

    def index_of_top(self, stack_num):
        offset = stack_num * self.stack_capacity
        return offset + self.sizes[stack_num] - 1


"""
Note: The Flexible Divisions approach, due to its complexity and the need for a detailed implementation that includes dynamic resizing, shifting of elements, and possibly wrapping around the array, is not fully implemented here. 
It's a more advanced method suited for those looking for a challenge beyond the scope of typical interview questions.

This Python solution focuses on the Fixed Division approach, providing a clear, efficient, and straightforward way to manage three stacks within a single array, alongside detailed complexity analyses for both outlined methods.
"""
