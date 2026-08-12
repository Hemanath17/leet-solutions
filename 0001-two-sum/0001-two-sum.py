class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_nums = [(num, i) for i, num in enumerate(nums)]
        index_nums.sort()
        l, r = 0, len(index_nums) - 1
        while l < r:
            currentsum = index_nums[l][0] + index_nums[r][0]
            if currentsum > target:
                r -= 1
            elif currentsum < target:
                l += 1
            else:
                return [index_nums[l][1], index_nums[r][1]]
        return []
