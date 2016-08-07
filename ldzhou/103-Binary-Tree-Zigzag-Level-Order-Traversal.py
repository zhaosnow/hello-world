# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = list()
        layer = list()
        queue = list()
        queue.append(root)
        queue.append('#')
        zigzag = True
        
        while queue:
            front = queue.pop(0)
            if front == '#':
                if queue:
                    queue.append('#')
                if zigzag:
                    ans.append(layer)
                else:
                    ans.append(layer[::-1])
                layer = []
                zigzag = not zigzag
            else:
                layer.append(front.val)
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)
        return ans
