"""
[LeetCode]141. Linked List Cycle

Problem Statement:
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle exists if a node can be reached again by continuously following the next pointer.

Example:
Input: head = [3,2,0,-4], pos = 1 (where tail connects to the 1st node)
Output: true

Approach:
Use Floyd's Tortoise and Hare algorithm, which employs two pointers moving at different speeds to detect cycles.

Complexity Analysis:
- Time Complexity: O(N), where N is the number of nodes in the linked list. In the worst case, each node is visited once.
- Space Complexity: O(1), as only two pointers are used regardless of the size of the input list.

Solution Implementation:
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow = head  # Moves one step at a time
        fast = head.next  # Moves two steps at a time

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True  # The fast and slow pointers meet, indicating a cycle


# Example usage is not applicable as it requires creating a linked list with a cycle,
# which cannot be easily represented in a simple text format.
