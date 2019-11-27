class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        res = {}
        for word in A.split(" "):
            if word not in res: res[word] = 0
            
            res[word] += 1
        for word in B.split(" "):
            if word not in res: res[word] = 0
            
            res[word] += 1
            
        return [word for word, val in res.items() if val == 1]
        