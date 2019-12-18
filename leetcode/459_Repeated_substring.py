# Confusing solution
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not str:
            return False
            
        ss = (s + s)[1:-1]
        return ss.find(s) != -1

# Kevin's solution
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False
        string_length = len(s)
        for i in range(1, string_length//2 + 1):
            substring = s[0:i]
            if substring * (string_length // i) == s:
                return True
        return False