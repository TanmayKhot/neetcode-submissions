class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        s = set(nums)
        res = 0

        for i in nums:
            if not i-1 in s:
                new_res = 1
                while i+1 in s:
                    new_res += 1
                    i += 1
                res = max(res,new_res)
        
        return res