def postorder(root,l):
    if(root==None):
        return
    postorder(root.left,l)
    postorder(root.right,l)
    l.append(root.val)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        postorder(root,l)
        return l
