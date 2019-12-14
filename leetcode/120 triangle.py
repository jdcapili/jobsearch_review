class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        f = [0] * (len(triangle) + 1)
        for row in triangle[::-1]: # reversed iteration on the 2d array.
            for i in range(len(row)):
                f[i] = row[i] + min(f[i], f[i + 1])
        return f[0]