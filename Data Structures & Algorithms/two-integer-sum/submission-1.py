class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subs = set()
        for i in range(len(nums)):
            if target - nums[i] in subs:
                return [nums.index(target-nums[i]),i]
            else:
                subs.add(nums[i])
        