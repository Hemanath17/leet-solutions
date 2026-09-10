class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        result=0
        l = 0
        zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros +=1
            while zeros>k:
                if nums[l] == 0:
                    zeros-=1
                l+=1
            result = max(result, i-l+1)
        return result