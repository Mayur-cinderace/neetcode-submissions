class Solution:
    def pre(self, root, t):
        if root == None:
            return
        t.append(root.val)
        self.pre(root.left, t)
        self.pre(root.right, t)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.pre(root, res)
        return res