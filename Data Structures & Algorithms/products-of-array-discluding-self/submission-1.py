class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # if len(nums) == 2:
        #     return [nums[1], nums[0]]
        prefixSumLeft = [1]*(len(nums))
        prefixSumRight = [1]*(len(nums))
        for i in range(len(nums)):
            prefixSumLeft[i] = prefixSumLeft[i-1] * nums[i]

        prefixSumRight[-1] = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            prefixSumRight[i] = nums[i] * prefixSumRight[i+1]
        
        answer = [prefixSumRight[1]]
        for i in range(1,len(nums)-1):
            answer.append(prefixSumLeft[i-1]*prefixSumRight[i+1])
        answer.append(prefixSumLeft[-2])
        return answer
        