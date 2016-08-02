# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#这道题的实现非常的巧妙, 使用一个stack, 存放从root到leaf的路径节点, 保证每个加点出栈, 入栈一次. # 突然发现, 是利用一个栈, 实现了中序遍历
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.path = list()
        self.pushall(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.path) > 0 #判断path是否为空

    def next(self):
        """
        :rtype: int
        """
        temp = self.path.pop()
        self.pushall(temp.right)
        return temp.val
            
    def pushall(self, root): # 将root到最左leaf的路径输入到path中, 保证path的最后一个元素是最小的. 每个node只会进path一次
        cur = root
        while cur:
            self.path.append(cur)
            cur = cur.left
            
# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
