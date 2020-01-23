class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        first = nums[0]
        rest = nums[1:]
        allPerm = []
        for permutation in self.permute(rest):
            for i in range(len(permutation)+1):
                newPerm = permutation[:i] + [first] + permutation[i:]
                allPerm.append(newPerm)
        return allPerm