def length(head):
    cnt=0
    while(head!=None):
        cnt+=1
        head=head.next
    return cnt
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l1=[]
        l2=[]
        n=length(head)
        i=0
        while(head!=None and i<n):
            if(i%2==0):
                l1.append(head.val)
            else:
                l2.append(head.val)
            head=head.next
            i+=1
        l3=l1+l2
        nn=ListNode(0)
        tmp=nn
        for i in range(len(l3)):
            n=ListNode(l3[i])
            nn.next=n
            nn=nn.next
        return tmp.next
            
