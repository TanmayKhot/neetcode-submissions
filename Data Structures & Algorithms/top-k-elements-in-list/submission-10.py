class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = Counter(nums)
        print(d)

        sorted_dict = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        res = list(sorted_dict)

        return res[:k]