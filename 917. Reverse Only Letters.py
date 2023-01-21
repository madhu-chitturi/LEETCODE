                                              917. Reverse Only Letters
  
  class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        a=list(s)
        n=len(a)
        i=0
        j=n-1
        while(i<j):
            if a[i].isalpha() and a[j].isalpha():
                tmp=a[i]
                a[i]=a[j]
                a[j]=tmp
                i+=1
                j-=1
            else:
                if a[i].isalpha():
                    j-=1
                else:
                    i+=1
        return "".join(a)
        
