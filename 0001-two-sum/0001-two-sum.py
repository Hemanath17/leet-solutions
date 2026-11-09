class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevmap = {}
        for i in range(len(nums)):
            total = target - nums[i]
            if total in prevmap:
                return [prevmap[total],i]
            prevmap[nums[i]] = i
        
