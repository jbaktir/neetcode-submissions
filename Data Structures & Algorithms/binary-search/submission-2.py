class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r-l) // 2)
            if nums[m] < target:
                l = m + 1
                if l <= r and nums[l] == target:
                    return l
            elif nums[m] > target:
                r = m - 1
                if r >= l and nums[r] == target:
                    return r
            else:
                return m
        return -1