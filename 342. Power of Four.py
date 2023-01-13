class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if(n==4 or n==1):
            return True
        elif(n>4):
            n=n/4
            return self.isPowerOfFour(n)
        else:
            return False
