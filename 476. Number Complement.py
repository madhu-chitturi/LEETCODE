class Solution:
    def findComplement(self, num: int) -> int:
        a=list(bin(num))
        print(a)
        a.pop(0)
        a.pop(0)
        for i in range(len(a)):
            if(a[i]=='0'):
                a[i]='1'
            else:
                a[i]='0'
        c="".join(a)
        return int(c,2)
