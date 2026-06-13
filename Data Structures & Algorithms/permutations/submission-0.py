class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = set() # Keeps track of numbers currently in the path
        
        def backtrack(current_path):
            if len(current_path) == len(nums):
                result.append(list(current_path))
                return
            
            for num in nums:
                # Lookups in a set are O(1), which is much faster than O(n) in a list
                if num in visited:
                    continue
                
                # 1. Choose
                current_path.append(num)
                visited.add(num) # Mark as used
                
                # 2. Explore
                backtrack(current_path)
                
                # 3. Un-choose
                current_path.pop()
                visited.remove(num) # Mark as free again

        backtrack([])
        return result