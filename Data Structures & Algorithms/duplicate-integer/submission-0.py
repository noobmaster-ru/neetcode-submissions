class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for elem in nums:
            if elem not in unique:
                unique.add(elem)
            else:
                return True
        return False