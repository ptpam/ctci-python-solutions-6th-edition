"""
Recursive Multiply

Problem Statement:
Write a method to multiply two positive integers without using the '*' (multiplication) or '/' (division) operators. 
You can use addition, subtraction, and bit shifting. The goal is to minimize the number of those operations.

Solution Overview:
1. Brute Force: Directly simulate the multiplication process through repeated addition.
2. With Memoization: Optimize by caching intermediate results to avoid redundant calculations.
3. Optimized for Even and Odd: Further optimize by reducing recursive calls, especially for odd numbers.

Complexity Analysis:
- Brute Force: Time Complexity is O(b) where b is the smaller of the two numbers.
- With Memoization: Time Complexity improves to O(log b), reducing redundant operations.
- Optimized for Even and Odd: Also O(log b), but typically requires fewer recursive calls than the memoization approach, especially for odd numbers.
"""


def minProductBruteForce(a, b):
    """Brute Force approach."""
    bigger = b if a < b else a
    smaller = a if a < b else b
    return minProductHelperBruteForce(smaller, bigger)


def minProductHelperBruteForce(smaller, bigger):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger
    return bigger + minProductHelperBruteForce(smaller - 1, bigger)


def minProductMemo(a, b):
    """Optimization with memoization."""
    bigger = b if a < b else a
    smaller = a if a < b else b
    memo = [0] * (smaller + 1)
    return minProductHelperMemo(smaller, bigger, memo)


def minProductHelperMemo(smaller, bigger, memo):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger
    if memo[smaller] > 0:
        return memo[smaller]

    s = smaller >> 1
    side1 = minProductHelperMemo(s, bigger, memo)
    side2 = (
        side1 if smaller % 2 == 0 else minProductHelperMemo(smaller - s, bigger, memo)
    )
    memo[smaller] = side1 + side2
    return memo[smaller]


def minProductOptimized(a, b):
    """Optimized for even and odd numbers."""
    bigger = b if a < b else a
    smaller = a if a < b else b
    return minProductHelperOptimized(smaller, bigger)


def minProductHelperOptimized(smaller, bigger):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger

    s = smaller >> 1
    halfProd = minProductHelperOptimized(s, bigger)
    if smaller % 2 == 0:
        return halfProd + halfProd
    else:
        return halfProd + halfProd + bigger


# Example usage
if __name__ == "__main__":
    a, b = 8, 7
    print("Brute Force:", minProductBruteForce(a, b))
    print("With Memoization:", minProductMemo(a, b))
    print("Optimized for Even and Odd:", minProductOptimized(a, b))
