class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset = []

        def backtrack(i, subset, total):
            
            # Stopping condition
            # Either success or stopping case
            if total == target:
                res.append(subset.copy())
                return
            if i >= len(nums) or total > target:
                return

            # Include the current number in the final subset
            subset.append(nums[i])
            backtrack(i, subset, total + nums[i])

            # Exclude the current number from final subset
            subset.pop()
            backtrack(i+1, subset, total)

        backtrack(0, [], 0)

        return res
