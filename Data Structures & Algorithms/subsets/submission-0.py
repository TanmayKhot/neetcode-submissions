class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []

        def backtrack(i):

            # Stopping case
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # Include option
            subset.append(nums[i])
            backtrack(i+1)

            # Exclude option
            subset.pop()
            backtrack(i+1)
        
        backtrack(0)
        return res