class Solution:
    def defangIPaddr(self, address: str) -> str:
        a=list(address)
        for i in range(len(a)):
            if(a[i]=='.'):
                a[i]='[.]'
        s=a[0]
        for k in range(1,len(a)):
            s+=a[k]
        return s
