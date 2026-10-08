class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        result1 = list(set1-set2)
        result2 = list(set2-set1)
        return [result1, result2]