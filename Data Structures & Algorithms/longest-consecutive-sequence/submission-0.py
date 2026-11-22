class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set()

        for elem in nums:
            if elem not in hash_set:
                hash_set.add(elem)
        
        maxLength = 0
        for elem in hash_set:
            if elem+1 not in hash_set:
                maxL = 0
                while True:
                    maxL += 1
                    if elem - 1 not in hash_set:
                        break
                    elem -= 1
                if maxL > maxLength:
                    maxLength = maxL
        return maxLength