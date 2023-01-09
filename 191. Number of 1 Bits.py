class Solution:
    def hammingWeight(self, n: int) -> int:
        a=list(bin(n))
        c=a.count('1')
        return c
