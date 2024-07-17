class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        stack = [(None, root)]
        to_delete = set(to_delete)
        
        while stack:
            parent, current = stack.pop()
            if not current: continue
            
            if current.val in to_delete:
                stack.append((None, current.left))
                stack.append((None, current.right))
            else:
                if current.left and current.left.val in to_delete:
                    stack.append((None, current.left.left))
                    stack.append((None, current.left.right))
                    current.left = None
                else:
                    stack.append((current, current.left))
                    
                
                if current.right and current.right.val in to_delete:
                    stack.append((None, current.right.left))
                    stack.append((None, current.right.right))
                    current.right = None
                else:
                    stack.append((current, current.right))
                    
                # define the termination condition is when the parent is None and value isn't to be deleted
                if parent is None and current.val not in to_delete:
                    res.append(current)
                    
        return res