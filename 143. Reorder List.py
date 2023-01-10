def findmid(head):
    slow=head
    fast=head
    while(fast.next!=None and fast.next.next!=None):
        slow=slow.next
        fast=fast.next.next
    return slow
def reverse(head):
    prev=None
    while(head!=None):
        tmp=head.next
        head.next=prev
        prev=head
        head=tmp
    return prev
def join(head,rev):
    tmp=head
    while(head!=None and rev!=None):
        tmp1=head.next
        tmp2=rev.next
        head.next=rev
        rev.next=tmp1
        head=tmp1
        rev=tmp2
    return tmp
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid=findmid(head)
        sh=mid.next
        mid.next=None
        rev=reverse(sh)
        return join(head,rev)
