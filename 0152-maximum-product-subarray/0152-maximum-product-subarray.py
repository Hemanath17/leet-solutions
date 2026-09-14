class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = nums[0]
        current_min = nums[0]
        answer = nums[0]
        for n in nums[1:]:
            old_max = current_max
            old_min = current_min
            current_max = max(n,n*old_max, n*old_min)
            current_min = min(n,n*old_max, n*old_min)
            answer = max(answer, current_max)
        return answer