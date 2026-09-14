class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        ans = nums[0]
        for n in nums[1:]:
            current_sum = max(n, current_sum+n)
            ans = max(ans, current_sum)
        return ans