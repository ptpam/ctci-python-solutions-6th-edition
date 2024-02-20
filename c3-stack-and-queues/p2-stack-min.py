"""
[LeetCode]155. Min Stack

Problem Statement:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Example:
Input: ["MinStack","push","push","push","getMin","pop","top","getMin"]
       [[],[-2],[0],[-3],[],[],[],[]]
Output: [null,null,null,null,-3,null,0,-2]

Explanation:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:
- Methods pop, top and getMin operations will always be called on non-empty stacks.
- At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
- -2^31 <= val <= 2^31 - 1

Solution Approach:
The MinStack class is designed to operate in O(1) time complexity for each of its methods. It maintains two stacks:
1. `stack` - A standard stack to store all the elements.
2. `order` - A stack to keep track of the minimum element at every push operation.

The `order` stack is the key to ensuring that the getMin() operation has O(1) complexity by keeping track of the current minimum element for every state of the `stack`.

Solution Implementation:
"""


class MinStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.order = []

    def push(self, val: int) -> None:
        """
        Push element val onto stack.
        """
        self.stack.append(val)
        # Update the order stack with the new min value after each push
        min_elem = val if not self.order else min(val, self.order[-1])
        self.order.append(min_elem)

    def pop(self) -> None:
        """
        Removes the element on top of the stack.
        """
        if self.stack:
            self.stack.pop()
            self.order.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        """
        Retrieve the minimum element in the stack.
        """
        return self.order[-1] if self.order else None


# Example of usage:
if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print("Minimum:", minStack.getMin())  # Returns -3
    minStack.pop()
    print("Top:", minStack.top())  # Returns 0
    print("Minimum:", minStack.getMin())  # Returns -2

"""
The MinStack class provides an efficient way to maintain a stack data structure that can return the minimum element in constant time. 
By leveraging an auxiliary stack (`order`), the class ensures that all operations perform as required by the problem statement.
"""
