class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        s = set(nums)
        res = 1

        for i in range(len(nums)):
            x = nums[i]
            new_res = 1
            while x+1 in s:
                x += 1
                new_res += 1
            res = max(res, new_res)
        
        return res
            