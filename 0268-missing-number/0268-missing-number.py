class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actual = sum(nums)
        expected =n*(n+1)//2
        return expected-actual