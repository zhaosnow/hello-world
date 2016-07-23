# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = list()
        ans = list()
        layer = list()
        queue.append(root)
        queue.append('#')
        
        while queue:
            front = queue.pop(0)
            if front == '#':
                if queue:
                    queue.append('#')
                ans.append(layer[-1])
                layer = []
            else:
                layer.append(front.val)
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)
        return ans
