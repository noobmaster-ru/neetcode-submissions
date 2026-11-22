class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for elem in nums:
            if elem not in freq:
                freq[elem] = 1
            else:
                freq[elem] += 1
        sorted_freq = sorted(freq.items(), reverse=True, key = lambda pair: pair[1])[:k]
        print(sorted_freq)
        return [elem[0] for elem in sorted_freq]


