"""
Towers of Hanoi

Problem Statement:
In the Towers of Hanoi puzzle, you have 3 towers and N disks of different sizes which can slide onto any tower. The puzzle starts with the disks in ascending order of size from top to bottom on the first tower. The objective is to move all the disks to the last tower while adhering to the following rules:
1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack.
3. No disk may be placed on top of a smaller disk.

This problem is solved using a recursive strategy, where disks are moved between towers with the help of a buffer tower.

Approach:
- Recursively move the top n-1 disks from the origin to the buffer tower, using the destination as a buffer.
- Move the nth disk (the largest one) from the origin to the destination tower.
- Recursively move the n-1 disks from the buffer to the destination tower, using the origin as a buffer.

Complexity Analysis:
- Time Complexity: O(2^n), where n is the number of disks. Each move involves a recursive call that approximately doubles the number of steps.
- Space Complexity: O(n) for the recursive call stack depth.

Solution Implementation:
"""


class Tower:
    def __init__(self, i):
        self.disks = []
        self.index = i

    def index(self):
        return self.index

    def add(self, d):
        if self.disks and self.disks[-1] <= d:
            print(f"Error placing disk {d}")
        else:
            self.disks.append(d)

    def moveTopTo(self, t):
        top = self.disks.pop()
        t.add(top)

    def moveDisks(self, n, destination, buffer):
        if n <= 0:
            return
        self.moveDisks(n - 1, buffer, destination)
        self.moveTopTo(destination)
        buffer.moveDisks(n - 1, destination, self)


def main():
    n = 3  # Number of disks
    towers = [Tower(i) for i in range(3)]
    for i in range(n - 1, -1, -1):
        towers[0].add(i)
    towers[0].moveDisks(n, towers[2], towers[1])
    print([tower.disks for tower in towers])


if __name__ == "__main__":
    main()
