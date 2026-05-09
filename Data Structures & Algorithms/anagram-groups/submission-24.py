class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(lambda: [])
        for i in strs:
            res = tuple(sorted(Counter(i).items()))
            d[res].append(i)


        return list(d.values())