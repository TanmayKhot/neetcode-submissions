class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = Counter(nums)
        freqs = [[] for _ in range(len(nums)+1)]

        for key,value in counts.items():
            freqs[value].append(key)

        res = []

        for i in range(len(freqs)-1, -1, -1):
            if freqs[i]:
                for j in range(len(freqs[i])):
                    res.append(freqs[i][j])
                    if len(res) == k:
                        return res