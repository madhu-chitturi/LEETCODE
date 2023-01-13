class Solution:
    def toLowerCase(self, s: str) -> str:
        a=list(s)
        for i in range(len(a)):
            if(ord(a[i])>=65 and ord(a[i])<=90):
                a[i]=a[i].lower()
        b=a[0]
        for j in range(1,len(a)):
            b+=a[j]
        return b
