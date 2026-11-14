class Solution:
    def trap(self, height: List[int]) -> int:
        
        lefts = [0] * len(height)
        rights = [0] * len(height)
        l_max = 0

        for i in range(len(height)):
            lefts[i] = l_max
            l_max = max(l_max, height[i])

        r_max = 0

        for i in range(len(height)-1,-1,-1):
            rights[i] = r_max
            r_max = max(r_max, height[i])
        
        res = 0
        for i in range(len(lefts)):

            if lefts[i] > 0 and rights[i] > 0:

                sum = min(lefts[i], rights[i]) - height[i]
                if sum > 0:
                    res += sum
                #print(i, sum,"||", lefts[i], rights[i])

        return res

