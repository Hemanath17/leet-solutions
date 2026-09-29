class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        seen = set(nums)
        result = []
        for n in range(1, len(nums)+1):
            if n not in seen:
                result.append(n)
        return result