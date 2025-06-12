def max_adjacent_diff(nums):
    maxDiff = 0
    length = len(nums)

    for i in range(length):
        next = (i + 1) % length
        difference = abs(nums[i] - nums[next])
        maxDiff = max(difference, maxDiff)
        return maxDiff
