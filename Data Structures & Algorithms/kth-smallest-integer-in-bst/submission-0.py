# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, k, req):
        if root == None:
            return 0
        self.inorder(root.left, k, req)  
        req.append(root.val)
        self.inorder(root.right, k, req)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        req = []
        self.inorder(root, k, req)
        return req[k-1]