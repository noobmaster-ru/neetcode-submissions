class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0]*n
        cache[0] = 1
        if n >= 2:
            cache[1] = 2
        if n >= 3:
            cache[2] = 3
        for i in range(3,n):
            cache[i] = cache[i-1] + cache[i-2]
        return cache[n-1]