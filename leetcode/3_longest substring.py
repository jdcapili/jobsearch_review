class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        current = ""
        for i in range(len(s)):
            if s[i] not in current:
                current += s[i]
            else:
                current = current[current.rfind(s[i])+1:len(current)]
                current += s[i]

            
            if current not in longest and len(current) > len(longest):
                longest = current
                
        return len(longest)

test = Solution()
test.lengthOfLongestSubstring(
"anviaj")