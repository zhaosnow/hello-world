class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 0, num
        while left <= right:
            mid = (left + right) // 2
            f = mid ** 2
            if f == num:
                return True
            elif f < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
