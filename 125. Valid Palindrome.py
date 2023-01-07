                                                                    125. Valid Palindrome
  
  class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=list(s)
        c=[]
        for i in range(len(a)):
            if(ord(a[i])>=65 and ord(a[i])<=90):
                b=a[i].lower()
                c.append(b)
            elif(ord(a[i])>=97 and ord(a[i])<=122):
                c.append(a[i])
            elif(a[i]>='0' and a[i]<='9'):
                c.append(a[i])
            else:
                pass
        d=c[::-1]
        if(c==d):
            return True
        else:
            return False
        
