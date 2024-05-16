# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        k=0
        while n>k:
            m = k+ (n-k)//2
            if  isBadVersion(m):
                n = m
            if not isBadVersion(m):
                k = m+1
        return k
