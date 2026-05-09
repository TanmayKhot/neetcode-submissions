class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(lambda: [])
        for i in strs:
            base = [0] * 26
            for s in i:
                idx = ord(s) - ord('a')
                base[idx] += 1
            d[tuple(base)].append(i)

        print(d.values())
        return list(d.values())