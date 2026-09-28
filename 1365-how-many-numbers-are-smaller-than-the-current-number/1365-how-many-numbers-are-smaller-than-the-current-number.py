class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        sorted_nums = sorted(nums)
        rank = {}
        for i, n in enumerate(sorted_nums):
            if n not in rank:
                rank[n] =i
        return [rank[n] for n in nums]