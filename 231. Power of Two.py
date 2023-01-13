class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if(n==2 or n==1):
            return True
        elif(n>2):
            n=n/2
            return self.isPowerOfTwo(n)
        else:
            return False
