                                                              20. Valid Parentheses               
  LINK:https://leetcode.com/problems/valid-parentheses/description/
      
 class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        a=list(s)
        n=len(a)
        if(n==1):
            return False
        else:
            for i in range(n):
                if(a[i]=='('):
                    
                    stack.append(a[i])
                elif(a[i]==')'):
                    if(len(stack)!=0):
                        if(stack[(len(stack)-1)]=='('):
                            stack.pop()
                        else:
                            return False
                    else:
                        return False
                if(a[i]=='{'):
                    stack.append(a[i])
                elif(a[i]=='}'):
                    if(len(stack)!=0):
                        if(stack[(len(stack)-1)]=='{'):
                            stack.pop()
                        else:
                            return False
                    else:
                        return False
                if(a[i]=='['):
                    stack.append(a[i])
                elif(a[i]==']'):
                    if(len(stack)!=0):
                        if(stack[(len(stack)-1)]=='['):
                            stack.pop()
                        else:
                            return False
                    else:
                        return False
            if(len(stack)==0):
                return True
            else:
                return False
           
