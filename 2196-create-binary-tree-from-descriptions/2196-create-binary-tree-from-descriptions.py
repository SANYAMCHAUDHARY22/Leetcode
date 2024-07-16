class Solution:
    def createBinaryTree(self, a: List[List[int]]) -> Optional[TreeNode]:
        d, q = {}, set()
        for p,c,l in a:
            setattr(d.setdefault(p, TreeNode(p)), ('right', 'left')[l], d.setdefault(c, TreeNode(c)))
            q.add(c)
        
        return d[({*d} - q).pop()]