class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        global l
        l=[]
        def f(root,s):
            if(root is None):
                pass
            elif(root.left is None and root.right is None):
                s+=str(root.val)
                l.append(s)
            else:
                s+=str(root.val)
                s1=s[::]
                f(root.left,s)
                f(root.right,s1)
        f(root,"")
        ans=0
        for i in l:
            ans+=int(i)
        return ans