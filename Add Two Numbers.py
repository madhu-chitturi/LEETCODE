                                                            Add Two Numbers
 Link:https://leetcode.com/problems/add-two-numbers/description/
 
 # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n=ListNode(0)
        t=n
        c=0
        while(l1!=None and l2!=None):
            s=l1.val+l2.val+c
            a=s%10
            b=ListNode(a)
            n.next=b
            n=n.next
            c=s//10
            l1=l1.next
            l2=l2.next
        while(l1!=None):
            s=l1.val+c
            a=s%10
            b=ListNode(a)
            n.next=b
            n=n.next
            c=s//10
            l1=l1.next
        while(l2!=None):
            s=l2.val+c
            a=s%10
            b=ListNode(a)
            n.next=b
            n=n.next
            c=s//10
            l2=l2.next
        if(c==1):
            n1=ListNode(1)
            n.next=n1
            n=n.next
        return t.next
