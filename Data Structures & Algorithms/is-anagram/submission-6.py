class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        ds = defaultdict(lambda: 0)
        dt = defaultdict(lambda: 0)

        for i in s:
            if i not in ds:
                ds[i] = 1 
            else:
                ds[i] += 1
        
        for i in t:
            if i not in dt:
                dt[i] = 1 
            else:
                dt[i] += 1

        return ds == dt
        