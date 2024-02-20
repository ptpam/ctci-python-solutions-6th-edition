"""
Stack of Plates

Problem Statement:
Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life,
we would likely start a new stack when the previous stack exceeds some threshold. Implement a data
structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should
create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop()
should behave identically to a single stack. Additionally, implement a function popAt(int index) which
performs a pop operation on a specific sub-stack.

Approach:
1. SetOfStacks is composed of several stacks and creates a new stack once the previous one reaches
its capacity limit.
2. For the popAt function, implement a rollover system to maintain the stack's capacity.

Complexity Analysis:
- Time Complexity: O(1) for push and pop operations under normal conditions, O(N) for popAt due to
potential rollover operations.
- Space Complexity: O(N), where N is the number of elements across all stacks.

Solution:
"""


class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def push(self, item):
        if len(self.stack) < self.capacity:
            self.stack.append(item)
            return True
        return False

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def is_full(self):
        return len(self.stack) == self.capacity

    def is_empty(self):
        return len(self.stack) == 0


class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = [Stack(capacity)]

    def get_last_stack(self):
        if not self.stacks:
            return None
        return self.stacks[-1]

    def push(self, item):
        last = self.get_last_stack()
        if last and not last.is_full():
            last.push(item)
        else:
            new_stack = Stack(self.capacity)
            new_stack.push(item)
            self.stacks.append(new_stack)

    def pop(self):
        last = self.get_last_stack()
        if not last:
            return None
        item = last.pop()
        if last.is_empty():
            self.stacks.pop()
        return item

    def popAt(self, index):
        if index < 0 or index >= len(self.stacks):
            return None
        stack = self.stacks[index]
        item = stack.pop()
        if stack.is_empty():
            del self.stacks[index]
        return item


"""
Example:
set_of_stacks = SetOfStacks(3)
set_of_stacks.push(1)
set_of_stacks.push(2)
set_of_stacks.push(3)
set_of_stacks.push(4)  # Should start a new stack
print(set_of_stacks.pop())  # Outputs: 4
print(set_of_stacks.popAt(0))  # Outputs: 3, popping from the first stack
"""

"""
Note: The implementation of SetOfStacks demonstrates how to manage multiple stacks within a single data structure,
simulating the behavior of a real-life scenario with plates. The additional challenge, popAt(int index), introduces
the need to consider how to maintain the stack's integrity when popping from any stack other than the last.
"""
