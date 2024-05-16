from operator import and_, or_


class Solution:
	"""
	Time:   O(n)
	Memory: O(n)
	"""

	MAPPING = {
		0: lambda *_: False,
		1: lambda *_: True,
		2: or_,
		3: and_,
	}

	def evaluateTree(self, root: Optional[TreeNode]) -> bool:
		if root is not None:
			return self.MAPPING[root.val](
				self.evaluateTree(root.left),
				self.evaluateTree(root.right),
			)