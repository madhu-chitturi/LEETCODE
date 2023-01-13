def depth(root,c):
    if(root==None):
        return c
    return max(depth(root.left,c+1),depth(root.right,c+1))
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        c=0
        return depth(root,c)
