# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorder(root,l):
    if root==None:
        return
    inorder(root.left,l)
    l.append(root.val)
    inorder(root.right,l)
def mode(l):
    a=list(set(l))
    m=-1
    r=[]
    for i in range(len(a)):
        z=l.count(a[i])
        if(m==z):
            r.append(a[i])
        elif(m<z):
            r.clear()
            r.append(a[i])
            m=z
    return r

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        inorder(root,l)
        return mode(l)
