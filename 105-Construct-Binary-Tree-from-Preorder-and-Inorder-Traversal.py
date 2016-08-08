# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        root = self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
        return root
        
    def build(self, preorder, b1, e1, inorder, b2, e2):
        if b1 > e1:
            return None
        root = TreeNode(preorder[b1])
        inorder_index = b2
        
        while inorder[inorder_index] != root.val:
            inorder_index += 1
        root.left = self.build(preorder, b1 + 1, b1 + inorder_index - b2, inorder, b2, inorder_index - 1)
        root.right = self.build(preorder, b1 + inorder_index - b2 + 1, e1, inorder, inorder_index + 1, e2)
        return root
