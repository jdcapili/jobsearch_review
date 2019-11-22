# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

# Example 1:

# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
#              jump length is 0, which makes it impossible to reach the last index.

# REWORK

# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         if len(nums) == 1: return True
#         table = [False] * len(nums)
#         table[0] = True
        
#         for i in range(0,len(nums) - 1):
            
#             if table[i] == True:
#                 jump = i + nums[i]
#                 for j in range(i , i + nums[i] + 1):
#                     if j > len(table) - 1: break
#                     table[j] = True
#                     if table[-1] is True: return True    
                        

        
#         return False


# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         if len(nums) == 1: return True
#         if nums[0] == 0: return False
#         table = [False] * len(nums)
#         table[0] = True
        
#         for i in range(0,len(nums) - 1):
#             if nums[i] >= len(nums) - 1 - i and table[i] is True: 
#                 print('jump higher than range')
#                 return True
#             print(table)
#             if table[i] == True:
#                 jump = i + nums[i]
#                 for j in range(i , i + nums[i] + 1):
#                     if j > len(table) - 1: break
#                     table[j] = True
#                     if table[-1] is True: 
                        
#                         return True    
                        

        
#         return False

class Solution:
    def canJump(self, nums):
        table = set()


        def jump(start,table):
            
            print(table)
            jump_range = nums[start]
            # jump to new idx
            nxt = start + jump_range
            print(start,nxt,jump_range,len(nums) -1)
            # check value
            if nxt >= (len(nums) -1): 
                return True
            elif nxt in table: return
            else:
                table.add(nxt)
                while nxt > start:
                    if jump(nxt,table): return True
                    nxt -= 1
        # print(table)
        if jump(0,table): return True
        return False
    
test = Solution()
test.canJump(
[2,3,1,1,4])



