"""
Remove Duplicates from Unsorted Linked List

Problem Statement:
Given an unsorted linked list, remove duplicate nodes from the list.

Approach and Complexity Analysis:

1. O(N) Solution with Temporary Buffer:
   - Approach: Use a set to keep track of seen values. Iterate through the linked list, and remove nodes that contain values already in the set.
   - Time Complexity: O(N), where N is the number of nodes in the linked list. Each node is visited once.
   - Space Complexity: O(N), for storing seen node values in the set.

2. O(N^2) Follow-up Solution without Temporary Buffer:
   - Approach: Use a two-pointer technique to compare each node with every other node and remove duplicates.
   - Time Complexity: O(N^2), due to nested loops for comparison.
   - Space Complexity: O(1), as no extra space is used apart from temporary variables.

Solution Implementation:
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeDuplicatesO_N(self, head: ListNode) -> ListNode:
        if not head:
            return head

        seen = set()
        current = head
        seen.add(head.val)
        while current.next:
            if current.next.val in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.val)
                current = current.next
        return head

    def removeDuplicatesO_N2(self, head: ListNode) -> ListNode:
        current = head
        while current:
            runner = current
            while runner.next:
                if runner.next.val == current.val:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next
        return head


# Helper functions for testing
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


def main():
    # Example usage
    solution = Solution()
    linked_list = ListNode(
        12,
        ListNode(
            11, ListNode(12, ListNode(21, ListNode(41, ListNode(43, ListNode(21)))))
        ),
    )

    print("Original list:")
    printList(linked_list)

    # O(N) solution
    removed_duplicates_O_N = solution.removeDuplicatesO_N(linked_list)
    print("After removing duplicates with O(N) solution:")
    printList(removed_duplicates_O_N)

    # Resetting the list for O(N^2) solution
    linked_list = ListNode(
        12,
        ListNode(
            11, ListNode(12, ListNode(21, ListNode(41, ListNode(43, ListNode(21)))))
        ),
    )
    # O(N^2) solution
    removed_duplicates_O_N2 = solution.removeDuplicatesO_N2(linked_list)
    print("After removing duplicates with O(N^2) solution (Follow-up):")
    printList(removed_duplicates_O_N2)


if __name__ == "__main__":
    main()
