#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        cnt = 0
        def dfs(root):
            nonlocal cnt
            left = dfs(root.left) if root.left else 0
            right = dfs(root.right) if root.right else 0
            root.val += left + right
            cnt += abs(left) + abs(right)
            return root.val - 1
        
        dfs(root)

        return cnt