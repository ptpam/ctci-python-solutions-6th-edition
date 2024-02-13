"""
[LeetCode]86. Partition List

Problem Statement:
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x, preserving the original relative order of the nodes in each of the two partitions.

Example:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Approach:
- Create two dummy nodes: one for the "left" list to hold nodes less than x, and one for the "right" list to hold nodes greater than or equal to x.
- Traverse the original list, appending each node to the "left" list if its value is less than x, or to the "right" list otherwise.
- Connect the end of the "left" list to the beginning of the "right" list.
- Return the head of the "left" list, which now contains the partitioned nodes.

Complexity Analysis:
- Time Complexity: O(N), where N is the number of nodes in the linked list. Each node is visited exactly once.
- Space Complexity: O(1), as the extra space used does not depend on the input size of the list.

Solution Implementation:
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left_dummy = ListNode(0)
        right_dummy = ListNode(0)
        left = left_dummy
        right = right_dummy

        current = head
        while current:
            if current.val < x:
                left.next = current
                left = left.next
            else:
                right.next = current
                right = right.next
            current = current.next

        # Connect the end of the left list to the beginning of the right list
        left.next = right_dummy.next
        right.next = None  # End the right list

        return (
            left_dummy.next
        )  # The head of the left list now represents the partitioned list


# Helper function to print list nodes
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Example usage
if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
    x = 3
    print("Original list:")
    printList(head)

    partitioned_head = solution.partition(head, x)
    print("Partitioned list:")
    print
