class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        # ---------------------------
        def dfs(node, attr):
            
            if not node:
            
                # base case:
                # empty node or empty tree
                return 0
            
             
            if not node.left and not node.right:

                # base case:
                # current node is leaf node

                return node.val if attr == 'left' else 0

           
            # general case:
            return dfs(node.left, 'left') + dfs(node.right, 'right')
        
        # ---------------------------
        return dfs(node=root, attr='root')