class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        idx = 0
        result = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = nums[i] * prefix[i-1]
        
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                suffix[i] = nums[i] 
            else:
                suffix[i] = nums[i] * suffix[i+1]

        while idx < len(nums):
            if idx == 0:
                result[idx] = suffix[1]
            elif idx == len(nums) - 1:
                result[idx] = prefix[len(nums)-2]
            else:
                result[idx] = suffix[idx+1] * prefix[idx-1]
            
            idx+=1
            
        return result

        