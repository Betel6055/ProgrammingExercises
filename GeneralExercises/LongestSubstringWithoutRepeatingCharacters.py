class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # str_tmp = [i for i in s]
        # len_s = len(s)
        # for i in range(len_s):
        #     for j in range(len_s):
        #         if s[i] == str_tmp[j]:
        #             print(f'{i}:{j}')
        #     print('-'.center(20, '-'))
        # print(str_tmp)
        str_tmp = ''
        position = []
        for i in range(len(s)):
            if not(s[i] in str_tmp) and len(str_tmp) == 0:
                str_tmp += s[i]
                position.append(i)
            

        print(str_tmp)
        print(position)
        return len(str_tmp)

s = "abcabcbb"
object1 = Solution()
print(object1.lengthOfLongestSubstring(s))

