
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i=0
        n=len(arr)
        while(i<n):
            if(arr[i]==0):
                arr.pop(n-1)
                arr.insert(i+1,0)
                i+=2
            else:
                i+=1
                
        
