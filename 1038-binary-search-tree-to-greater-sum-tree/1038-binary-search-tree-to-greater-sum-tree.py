class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        s = 0
        def f(root):
            if root is None: return
            nonlocal s
            f(root.right)
            #print(s,root.val)
            s = s + root.val
            root.val = s
            f(root.left)
        f(root)
        return root