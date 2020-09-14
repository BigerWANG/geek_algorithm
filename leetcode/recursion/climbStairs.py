import functools


class Solution1:
    @functools.lru_cache(100)
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


s = Solution1()
print(s.climbStairs(38))
