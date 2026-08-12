class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # flag = False
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             flag = True
        # return flag

        # SEcond approach
        hash = dict()
        flag = False
        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        
        print(hash)

        for i in hash:
            if hash[i] > 1:
                flag = True
        return flag



            
        