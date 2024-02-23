"""
[LeetCode]49. Group Anagrams

Problem Statement:
Given an array of strings strs, group the anagrams together. 
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Examples:
1. Input: strs = ["eat","tea","tan","ate","nat","bat"]
   Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
2. Input: strs = [""]
   Output: [[""]]
3. Input: strs = ["a"]
   Output: [["a"]]

Constraints:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.

Solution Overview:
The solution involves categorizing each string by its character count. 
Since anagrams have the same number of each character, we can use this as a key in a hash map where each key maps to a list of anagrams. 
The final solution groups all anagrams based on this character count method.

Solution Details:
- Use a hash map to group words by their sorted character counts as keys.
- Iterate over each string in the input list, calculate its character count, and append it to the corresponding list in the hash map.
- Convert the hash map values into a list of lists to get the grouped anagrams.

Complexity Analysis:
- Time Complexity: O(N * K), where N is the number of strings in the input list and K is the maximum length of a string. The character count calculation is O(K), and we do this for each string.
- Space Complexity: O(N * K), to store the result. Each string is stored exactly once, and the character count array or tuple takes up to O(K) space per string.

Solution Implementation:
"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        ans = defaultdict(list)

        for s in strs:
            # Create a character count tuple for each string
            count = [0] * 26  # 26 for each lowercase English letter
            for c in s:
                count[ord(c) - ord("a")] += 1

            # Use the character count tuple as a key to group anagrams
            ans[tuple(count)].append(s)

        # Return the grouped anagrams as a list of lists
        return list(ans.values())


# Example of usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(solution.groupAnagrams([""]))
    print(solution.groupAnagrams(["a"]))

"""
This implementation groups anagrams by their character counts, providing an efficient solution to the problem. By mapping each string to a character count signature, anagrams naturally cluster together in the hash map, allowing for straightforward grouping.
"""
