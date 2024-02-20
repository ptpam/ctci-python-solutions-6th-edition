"""
[LeetCode]232. Implement Queue using Stacks

Problem Statement:
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
- void push(int x) Pushes element x to the back of the queue.
- int pop() Removes the element from the front of the queue and returns it.
- int peek() Returns the element at the front of the queue.
- boolean empty() Returns true if the queue is empty, false otherwise.

Constraints:
- 1 <= x <= 9
- At most 100 calls will be made to push, pop, peek, and empty.
- All the calls to pop and peek are valid.

Follow-up:
- Implement the queue such that each operation is amortized O(1) time complexity.

Example:
Input: ["MyQueue", "push", "push", "peek", "pop", "empty"]
       [[], [1], [2], [], [], []]
Output: [null, null, null, 1, 1, false]

Explanation:
MyQueue myQueue = new MyQueue();
myQueue.push(1);  // queue is: [1]
myQueue.push(2);  // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek();   // return 1
myQueue.pop();    // return 1, queue is [2]
myQueue.empty();  // return false

Solution Approach:
The queue is implemented using two stacks, `stack_in` for push operation and `stack_out` for pop and peek operations. 
The elements are moved from `stack_in` to `stack_out` to maintain the FIFO order using stack's LIFO nature.

Complexity Analysis:
- Each operation is amortized O(1) time complexity.

Solution Implementation:
"""


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of the queue.
        """
        self.stack_in.append(x)

    def pop(self) -> int:
        """
        Removes the element from the front of the queue and returns it.
        """
        self._move_in_to_out()
        return self.stack_out.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        self._move_in_to_out()
        return self.stack_out[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack_in and not self.stack_out

    def _move_in_to_out(self):
        """
        Move elements from stack_in to stack_out to maintain queue order.
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())


# Example of usage:
if __name__ == "__main__":
    myQueue = MyQueue()
    myQueue.push(1)
    myQueue.push(2)
    print("Peek:", myQueue.peek())  # Outputs: 1
    print("Pop:", myQueue.pop())  # Outputs: 1
    print("Empty:", myQueue.empty())  # Outputs: False

"""
This solution implements a queue using two stacks with all operations achieving O(1) amortized time complexity, fulfilling the problem requirements and the follow-up challenge.
"""
