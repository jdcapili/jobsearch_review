# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         longest = ""
#         current = ""
#         for i in range(len(s)):
#             for j in range(len(s)):
#                 subs = s[i:j+1]
#                 if self.isPalindrome(subs):

#                     longest = max([longest,subs],key=len)
                
#         return longest
        
    
#     def isPalindrome(self, s:str) -> bool:
#         cur = ""
        
#         while cur < s:
#             cur += s[-1]
#             s = s[0:-1]
        
#         if len(cur) > len(s):
#             return cur[:-1] == s
#         else: return cur == s

    # def longestPalindrome(self, s: str) -> str:
    #     l = len(s)
    #     if l < 2:
    #         return s
    #     ans = s[0]
    #     maxl = 1
    #     for i in range(l):
    #         j = 0
    #         while i + j < l and i - j >= 0 and s[i + j] == s[i - j]:
    #             print(i,j)
    #             j += 1
    #         if 2 * j - 1 > maxl:
    #             maxl = 2 * j - 1
    #             ans = s[i - j + 1:i + j]
    #     print(ans)
    #     for i in range(l):
    #         j = 0
    #         while i + j + 1 < l and i - j >= 0 and s[i + j + 1] == s[i - j]:
    #             j += 1
    #         if 2 * j > maxl:
    #             maxl = 2* j
    #             ans = s[i - j + 1: i + j + 1]
    #     print(ans)
    #     return ans


class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res
    
    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self, s, l, r):
        # print(l,r)
        while l >= 0 and r < len(s) and s[l] == s[r]:
            print(l,r)
            l -= 1; r += 1
        print(l,r)
        print(s[l+1:r])
        return s[l+1:r]
                

test = Solution()
print(test.longestPalindrome('ababa'))

