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

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = ""
        max_len = 0
        for char in s:
            if char not in curr: curr += char
            else:
                max_len = max(len(curr), max_len)
                start = curr.index(char)
                curr = curr[start+1:]+char
        return max(max_len, len(curr))

test = Solution()
test.lengthOfLongestSubstring(
"anviaj")