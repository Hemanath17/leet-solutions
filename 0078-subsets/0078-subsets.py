class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            new_subsets = []
            for existing_subset in result:
                new_subset = existing_subset + [num]
                new_subsets.append(new_subset)
            result = result + new_subsets
        return result