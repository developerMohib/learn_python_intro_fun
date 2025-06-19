class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        group = 1
        start = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[start] > k:
                group += 1
                start = i
        return group
