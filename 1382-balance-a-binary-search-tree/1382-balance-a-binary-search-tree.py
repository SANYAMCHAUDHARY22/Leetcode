class Solution:
    def inorder(self,root,lst):
        if root!=None:
            self.inorder(root.left,lst)
            lst.append(root.val)
            self.inorder(root.right,lst)
    def buildTree(self,lst,low,high):
        if low > high:
            return None
        mid = (low+high)//2
        root = TreeNode(lst[mid])
        root.left = self.buildTree(lst,low,mid-1)
        root.right = self.buildTree(lst,mid+1,high)
        return root

    def balanceBST(self, root: TreeNode) -> TreeNode:
        lst = []
        self.inorder(root,lst)
        low = 0
        high = len(lst)-1
        root = self.buildTree(lst,low,high)
        return root