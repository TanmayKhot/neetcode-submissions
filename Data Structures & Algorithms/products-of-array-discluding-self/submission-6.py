class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            a = 1
            for j in range(0,i,1):
                a *= nums[j]
            for j in range(i+1, len(nums), 1):
                a *= nums[j]
            
            res.append(a)
        
        return res


 