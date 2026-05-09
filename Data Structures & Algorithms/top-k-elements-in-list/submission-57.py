class Solution:
    def topKFrequent(self, nums: List[int], target: int) -> List[int]:

        d = Counter(nums)

        # O(nlogn) solution
        # sorted_dict = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        # res = list(sorted_dict)[:k]

        # Bucket sort O(n)
        buckets = [[] for i in range(len(nums) + 1)]

        for k,v in d.items():
            buckets[v].append(k)

        res= []
        for i in range(len(nums),-1,-1):
            if buckets[i]:
                for j in range(len(buckets[i])):
                    print(buckets[i])
                    res.append(buckets[i][j])
                    
    
                    target -= 1
                    print("RES", res, "K   ", target)
                    if target == 0:
                        return res
        
        return res




