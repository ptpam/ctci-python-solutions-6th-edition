"""
[LeetCode]19. Remove Nth Node From End of List

Problem Statement:
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Approach:
The solution utilizes a two-pointer technique with a dummy node to simplify edge cases. The first pointer (right) advances n steps ahead, and then both pointers (left and right) move together until right reaches the end of the list. The node following the left pointer is the one to be removed.

Complexity Analysis:
- Time Complexity: O(L), where L is the number of nodes in the linked list. The list is traversed at most twice - once to position the right pointer, and once to find the node to remove.
- Space Complexity: O(1), as the extra space used by the algorithm is constant and does not depend on the size of the input list.

Solution Implementation:
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)  # Create a dummy node to simplify removal logic
        left = dummy  # Left pointer starts at the dummy node
        right = head  # Right pointer starts at the head of the list

        # Move the right pointer n steps into the list
        while n > 0 and right:
            right = right.next
            n -= 1

        # Move both pointers until the right pointer reaches the end
        while right:
            left = left.next
            right = right.next

        # Delete the nth node from the end
        left.next = left.next.next

        return dummy.next  # Return the head of the modified list


# Helper function to print list nodes
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Example usage
if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2
    print("Original list:")
    printList(head)

    modified_head = solution.removeNthFromEnd(head, n)
    print(f"After removing the {n}th node from the end:")
    printList(modified_head)
