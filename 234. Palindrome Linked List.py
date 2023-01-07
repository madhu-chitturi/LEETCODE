                                                                234. Palindrome Linked List
  
  class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if(head.next==None):
            return True
        l=[]
        while(head!=None):
            l.append(head.val)
            head=head.next
        a=len(l)
        if(a%2==0):
            b=l[:a//2]
            c=l[a//2:]
        else:
            b=l[:a//2+1]
            c=l[a//2:]
            print(b)
            print(c)
        d=c[::-1]
        if(b==d):
            return True
        else:
            return False
