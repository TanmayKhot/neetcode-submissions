class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        l,r = 0,0
        res = []
        while l < len(s):
            while s[r] != '#' and r < len(s):
                r += 1
            num = int(s[l:r])
            res.append(s[r+1:r+1+num])
            l = r+1+num
            r = l

        
        return res

