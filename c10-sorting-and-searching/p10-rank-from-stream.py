"""
Rank from Stream

Problem Statement:
Implement data structures and algorithms to support the operations of tracking integers from a stream and retrieving the rank of a number x (number of values less than or equal to x).

Solution Overview:
Utilize a Binary Search Tree (BST) where each node also stores the size of its left subtree (number of nodes less than the node's value). This allows efficient tracking of integers and computation of ranks.

Solution Details:
- `track(int x)`: Inserts x into the BST. If x is less than or equal to the node, go left and increment the left subtree size. Otherwise, go right.
- `getRankOfNumber(int x)`: Computes the rank of x by traversing the BST. If moving left, the rank doesn't change. If moving right, increment the rank by the left subtree size plus one.

Complexity Analysis:
- Time Complexity: O(log N) on average for both track and getRankOfNumber, where N is the number of nodes in the tree. It degrades to O(N) in the worst case when the tree becomes unbalanced.
- Space Complexity: O(N) for storing the BST.

Solution Implementation:
"""


class RankNode:
    def __init__(self, value):
        self.value = value
        self.leftSize = 0
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = RankNode(value)
            self.leftSize += 1
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = RankNode(value)

    def getRank(self, value):
        if value == self.value:
            return self.leftSize
        elif value < self.value:
            if self.left is None:
                return -1
            else:
                return self.left.getRank(value)
        else:
            rightRank = -1 if self.right is None else self.right.getRank(value)
            if rightRank == -1:
                return -1
            else:
                return self.leftSize + 1 + rightRank


class StreamRank:
    def __init__(self):
        self.root = None

    def track(self, value):
        if self.root:
            self.root.insert(value)
        else:
            self.root = RankNode(value)

    def getRankOfNumber(self, value):
        if self.root:
            return self.root.getRank(value)
        return -1


# Example Usage
if __name__ == "__main__":
    sr = StreamRank()
    values = [5, 1, 4, 4, 5, 9, 7, 13, 3]
    for value in values:
        sr.track(value)
    print(f"Rank of 1: {sr.getRankOfNumber(1)}")  # Expected: 0
    print(f"Rank of 3: {sr.getRankOfNumber(3)}")  # Expected: 1
    print(f"Rank of 4: {sr.getRankOfNumber(4)}")  # Expected: 3
