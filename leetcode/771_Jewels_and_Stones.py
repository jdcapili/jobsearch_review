class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        c = 0
        for i in range(len(S)):
            if S[i] in J: c += 1
        return c