

def inorder(root):
    current = root
    stack = []
    l=[]
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif(stack):
            current = stack.pop()
            l.append(current.val)
            current = current.right
 
        else:
            break
    return l
      

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return inorder(root)
        
