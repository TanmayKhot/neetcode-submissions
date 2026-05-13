class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) < 2:
            return len(s)
        
        l = 0
        r = 1
        d = set()
        #.add(s[l])
        res = 0

        while r <= len(s):
            #print(s[l:r] , d)
            
            if s[r-1] not in d:
                d.add(s[r-1])
                res = max(res, r-l)
                #print("---" ,s[r-1] , d ,"Res:", res)
                r += 1
            else:
                while s[r-1] in d and l < r:
                    #print("... Removing", s[l])
                    d.remove(s[l])
                    #print("... Updated" ,d)
                    l += 1


        return res