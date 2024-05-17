class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root:
            root.left = self.removeLeafNodes(root.left, target)
            root.right = self.removeLeafNodes(root.right, target) 
            if root.val == target and not root.left and not root.right:
                root = None
        return root 