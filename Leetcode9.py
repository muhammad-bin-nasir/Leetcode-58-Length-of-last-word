"""Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        if (len(needle) > len(haystack)):
            return index
        for i in range(len(haystack)):
            if len(haystack)-i >= len(needle):
                if haystack[i] == needle[0]:
                    for j in range(len(needle)):
                        if needle[j] != haystack[i+j]:
                            index = -1
                            break
                        index = i
                    if (index != -1):
                        return index
            else:
                return index
        return index
                