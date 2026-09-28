class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        seen = set()
        duplicate = -1
        for n in nums:
            if n in seen:
                duplicate = n
            seen.add(n)
        for n in range(1, len(nums) + 1):
            if n not in seen:
                missing = n
                break
        return [duplicate, missing]