class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
        
        queue = [root]
        for _ in range(depth - 2):
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp

        for node in queue:
            temp = node.left;
            node.left = TreeNode(val)
            node.left.left = temp
            temp = node.right
            node.right = TreeNode(val)
            node.right.right = temp
            
        return root