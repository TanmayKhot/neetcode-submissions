from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a dictionary of counts automatically
        count = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]

        # Put numbers into buckets based on their frequency
        for num, cnt in count.items():
            freq[cnt].append(num)

        # Read buckets from right to left to get the highest frequencies
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res