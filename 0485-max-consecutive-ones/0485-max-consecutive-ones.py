class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        streak = 0
        res = 0
        for i in nums:
            if i==1:
                streak+=1
            else:
                streak = 0
            res = max(res,streak)
        return res