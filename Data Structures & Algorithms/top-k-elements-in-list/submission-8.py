class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        buckets = [[] for _ in range(len(nums) + 1)]
        count = Counter(nums)

        for num, freq in count.items():
            buckets[freq].append(num)
        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)

                if len(res) == k:
                    return res
        