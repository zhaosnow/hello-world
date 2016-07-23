class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        left = max(A, E)
        right = min(C, G)
        top = min(D, H)
        bottom = max(B, F)
        covered = 0
        if right > left and top > bottom:
            covered = (right - left) * (top - bottom)
        
        a = abs(C - A) * abs(D - B)
        b = abs(G - E) * abs(H - F)
        return a + b - covered
