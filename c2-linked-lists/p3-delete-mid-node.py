"""
[LeetCode]2095. Delete the Middle Node of a Linked List

Problem Statement:
You are given the head of a linked list. Delete the middle node and return the head of the modified linked list. The middle node is defined as the ⌊n / 2⌋th node from the start using 0-based indexing.

Example:
Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation: The middle node with value 7 is deleted.

Approach:
Use the two-pointer technique, with one pointer (fast) advancing twice for each step of the other pointer (slow). When the fast pointer reaches the end, the slow pointer will be at the node preceding the middle node. We then adjust the pointers to skip the middle node, effectively deleting it from the list.

Complexity Analysis:
- Time Complexity: O(N), where N is the number of nodes in the linked list. We traverse the list once.
- Space Complexity: O(1), as we only use a fixed number of pointers regardless of the input list size.

Solution Implementation:
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        # Edge case: if the list is empty or has only one node, return None
        if not head or not head.next:
            return None

        # Initialize two pointers
        slow = head
        fast = head.next.next

        # Move the fast pointer twice as fast as the slow pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Skip the middle node
        slow.next = slow.next.next

        return head


# Helper function to print list nodes
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Example usage
if __name__ == "__main__":
    solution = Solution()
    head = ListNode(
        1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6))))))
    )
    print("Original list:")
    printList(head)

    modified_head = solution.deleteMiddle(head)
    print("After deleting the middle node:")
    printList(modified_head)
