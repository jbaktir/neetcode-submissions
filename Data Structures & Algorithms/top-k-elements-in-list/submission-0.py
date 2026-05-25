class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        arr = []
        for key,v in counts.items():
            arr.append([v, key])
        arr.sort(key=lambda p: p[0])
        res = []
        for i in arr[-k:]:
            res.append(i[1])
        return res