class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = collections.defaultdict(int)
        
        for char in s:
            hash1[char] += 1
        
        for char in t:
            if char not in hash1:
                return False
            hash1[char] -= 1
            
        return all(val == 0 for val in hash1.values())