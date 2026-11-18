class Solution:
    def topKFrequent(self, nums: List[int], targett: int) -> List[int]:

        num_counts = dict(Counter(nums))
        d = {}

        for i in range(1,len(nums)+1):
            d[i] = []

        for k,v in num_counts.items():
            d[v].append(k)

        res = []
        target = targett
        for i in range(len(nums), -1, -1):
            if i in d:
                while target > 0 and d[i]:
                    temp = d[i].pop()
                    res.append(temp)
                    target -= 1
        
        return res

