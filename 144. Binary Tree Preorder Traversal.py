class Solution:
    if(root==None):
        return
    l.append(root.val)
    Solution.preorder(root.left,l)
    Solution.preorder(root.right,l)
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        x=Solution.preorder(root,l)
        return l
