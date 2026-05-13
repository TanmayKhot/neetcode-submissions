class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        for i in range(len(prefix)):
            res[i] = prefix[i] * suffix[i]

        return res





        # Brute Force
        # res = []
        # for i in range(len(nums)):
        #     a = 1
        #     for j in range(0,i,1):
        #         a *= nums[j]
        #     for j in range(i+1, len(nums), 1):
        #         a *= nums[j]
            
        #     res.append(a)
        
        # return res


 