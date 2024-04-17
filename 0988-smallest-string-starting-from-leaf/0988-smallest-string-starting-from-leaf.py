class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        return dfs(root)

def dfs(node, s=''):
    s = ascii_lowercase[node.val] + s
    if node.left and node.right:
        return min(dfs(node.left, s), dfs(node.right, s))
    elif child := node.left or node.right:
        return dfs(child, s)
    else:
        return s