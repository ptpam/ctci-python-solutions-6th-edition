"""
[LeetCode]125. Valid Palindrome

Problem Statement:
A phrase is considered a palindrome if, after converting all uppercase letters to lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Given a string s, determine if it is a palindrome.

Example:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: After cleaning, "amanaplanacanalpanama" is a palindrome.

Approach:
1. Clean the string by removing non-alphanumeric characters and converting to lowercase.
2. Use a two-pointer technique to compare characters from both ends, moving towards the center.

Complexity Analysis:
- Time Complexity: O(n), where n is the length of the string. Each character is visited at most twice - once during cleaning and once during the palindrome check.
- Space Complexity: O(n) for the cleaned string. In-place transformations could reduce this to O(1) in languages with mutable strings.

Solution Implementation:
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Clean the string
        cleaned = [char.lower() for char in s if char.isalnum()]

        # Two-pointer approach to check palindrome
        left, right = 0, len(cleaned) - 1
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left, right = left + 1, right - 1
        return True


# Example usage
if __name__ == "__main__":
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    print(f"The string '{s}' is a palindrome: {solution.isPalindrome(s)}")
