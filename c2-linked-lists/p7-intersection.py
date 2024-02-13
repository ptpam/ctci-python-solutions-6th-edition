"""
[LeetCode]349. Intersection of Two Linked Lists

Problem Statement:
Given the heads of two singly linked lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

Example:
Input: listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], intersectVal = 8
Output: Reference to node with value 8

Approach:
Use a two-pointer approach where each pointer starts at the heads of the two lists. When one pointer reaches the end of a list, it continues from the beginning of the other list. If the lists intersect, the pointers will meet at the intersection point. If not, they will both reach the end (null) simultaneously.

Complexity Analysis:
- Time Complexity: O(M+N), where M and N are the lengths of the two linked lists. Each pointer traverses at most M + N nodes.
- Space Complexity: O(1), as no extra space is used.

Solution Implementation:
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pointerA, pointerB = headA, headB

        # Continue until the two pointers meet or both reach the end (null)
        while pointerA is not pointerB:
            # If pointerA reaches the end, switch to headB. Otherwise, move to the next node.
            pointerA = pointerA.next if pointerA else headB
            # If pointerB reaches the end, switch to headA. Otherwise, move to the next node.
            pointerB = pointerB.next if pointerB else headA

        # Either both pointers are null (no intersection) or both point to the intersection node.
        return pointerA


# Helper function for testing
def createList(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


# Example usage
if __name__ == "__main__":
    solution = Solution()
    # Example: Creating intersecting lists manually for demonstration
    # List A: 4 -> 1 -> 8 -> 4 -> 5
    # List B: 5 -> 6 -> 1 -> [8 -> 4 -> 5] (intersect with list A at 8)
    common = createList([8, 4, 5])
    listA = createList([4, 1])
    listA.next.next = common
    listB = createList([5, 6, 1])
    listB.next.next.next = common

    print(f"Intersected at: '{solution.getIntersectionNode(listA, listB).val}'")
