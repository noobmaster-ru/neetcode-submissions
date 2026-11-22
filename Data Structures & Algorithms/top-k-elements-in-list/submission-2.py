class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for elem in nums:
            if elem not in freq:
                freq[elem] = 1
            else:
                freq[elem] += 1
        buckets = [[] for i in range(len(nums) + 1)]
        for elem, frequency in freq.items():
            buckets[frequency].append(elem)
        answer = []
        for i in range(len(buckets)-1,-1,-1):
            if k == 0:
                return answer
            if buckets[i] != [] and k > 0:
                for j in range(len(buckets[i])):
                    if k>0:
                        answer.append(buckets[i][j])
                        k -= 1
        return answer
            

    
        # sorted_freq = sorted(freq.items(), key = lambda pair: pair[1], reverse=True)[:k]
        # return [elem[0] for elem in sorted_freq]


