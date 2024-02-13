"""
[LeetCode]2. Add Two Numbers

Problem Statement:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. The two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Approach:
- Simulate the addition of two numbers as done manually, digit by digit.
- Keep track of the carry from each addition.
- Iterate over the digits of both numbers until all digits and the carry (if any) have been processed.

Complexity Analysis:
- Time Complexity: O(max(N,M)), where N and M are the lengths of l1 and l2, respectively. This is because we traverse the longest list completely.
- Space Complexity: O(max(N,M)), the length of the new list is at most max(N,M) + 1.

Solution Implementation:
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + carry
            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy_head.next


# Helper function to print list nodes
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Example usage
if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    print("Resultant list after addition:")
    result_head = solution.addTwoNumbers(l1, l2)
    printList(result_head)
