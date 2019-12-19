class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        
        for char in t:
            if char == s[0]:
                s = s[1:]
            if s == "":
                return True
        
        return False