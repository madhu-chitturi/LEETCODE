def length(head):
    cnt=0
    while(head!=None):
        cnt+=1
        head=head.next
    return cnt
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n=length(head)
        for i in range(n//2):
            head=head.next
        return head

        

