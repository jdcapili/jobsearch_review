class Solution:
    # def jump(self, nums):
    #     i = 0
    #     count = 0
    #     while i < len(nums)-1:
    
    #         if i + nums[i] >= len(nums) - 1:
    #             return count + 1
    #             end = len(nums)
    #         else:
    #             end = i + nums[i] + 1
        
    #         numslice = nums[i+1:end]
    #         m = max(numslice)
    #         i = [i for i, j in enumerate(numslice) if j == m][-1] + 1 + i
    #         count += 1


    #     return count
class Solution:
    def jump(self, nums):
        if len(nums) == 1: return 0
        min_steps = 0
        start_idx = 0
        furthest_idx = 0
        n_index = 0
        current_steps = nums[0]

        while current_steps > -1:

            if start_idx + current_steps >= len(nums) -1:
                min_steps += 1
                break
            if current_steps > 0:
                j = 1
                while j < current_steps + 1:
                    
                    if start_idx + j + nums[start_idx + j] > furthest_idx:
                        n_index = start_idx + j
                        furthest_idx = n_index + nums[start_idx + j]
                    j+=1
                start_idx = n_index
                current_steps = nums[start_idx]
                min_steps += 1
            else:
                min_steps += 1
                start_idx = n_index
                current_steps = nums[start_idx]
                furthest_idx = 0

        return min_steps
                        

test = Solution()
# test.jump([10,9,8,7,6,5,4,3,2,1,1,0])
test.jump([2,3,1,1,4])