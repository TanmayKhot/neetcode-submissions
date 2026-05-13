class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        r = 0
        l = 0
        res = 0
        d = set()

        for r in range(len(s)):
            while s[r] in d:
                d.remove(s[l])
                l += 1
            d.add(s[r])
            res = max(res , r-l+1)
        
        return res