'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_list = []
        str_tmp = ''
        str_len = 0

        for i in range(len(s)):
            if not(s[i] in str_tmp):
                str_tmp += s[i]
            else:
                str_list.append(str_tmp)
                str_tmp = ''
                str_tmp += s[i]

        str_list.append(str_tmp)

        for i in str_list:
            if str_len < len(i):
                str_len = len(i)

        return str_len

s = "dvdf"
object1 = Solution()
print(object1.lengthOfLongestSubstring(s))

