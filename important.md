# Important questions

<details>

<summary>  Top K Frequent Elements - Bucket sort  </summary>

https://neetcode.io/problems/top-k-elements-in-list/question

Using Counter/dictionary sorting will result in O(nlogn) <br>
Bucket sort gives it in O(n)

<b> Algorithm </b>
1. Build a frequency map that counts how many times each number appears.
2. Create a list of groups freq, where freq[i] will store all numbers that appear exactly i times.
3. For each number and its frequency in the map, add the number to freq[frequency].
4. Initialize an empty result list.
5. Loop from the largest possible frequency down to 1:<br>
     For each number in freq[i], add it to the result list.<br>
     Once the result contains k numbers, return it.

```python
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

        # Read buckets from right to left to get highest frequencies
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
```
</details>
