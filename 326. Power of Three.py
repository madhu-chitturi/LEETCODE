class Solution:
    def isPowerOfThree(self, n: int) -> bool: 
        if(n==3 or n==1):
            return True
        elif(n>3):
            n=n/3
            return self.isPowerOfThree(n)
        else:
            return False
