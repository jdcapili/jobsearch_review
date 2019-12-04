class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        res = [[1],[1,1]]
        i = 2
        while len(res) < numRows:
            prev = res[-1]
            nxt = []
            for i in range(len(prev)-1):
                nxt.append(prev[i]+prev[i+1])
            res.append([1] + nxt + [1])    
        return res