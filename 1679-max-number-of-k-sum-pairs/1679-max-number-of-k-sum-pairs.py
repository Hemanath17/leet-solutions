class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = len(nums)-1
        count=0
        while l<r:
            current_sum = nums[l]+nums[r]
            if current_sum == k:
                count+=1
                l +=1
                r -=1
            elif current_sum < k:
                l += 1
            else:
                r -= 1
        return count